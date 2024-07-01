# Best keyboard practices in SDL3.

***THIS PAGE IS STILL A WORK IN PROGRESS, WHICH IS WHY SOME SECTIONS DON'T HAVE CODE OR SPECIFIC SOLUTION DETAILS.***

## First things first

Keyboard input is a surprisingly complicated topic after you step outside of your usual country and language (and sometimes before you do, too).

Almost any game, no matter what approach it is taking, should probably offer a means for users to configure key bindings; not only will this solve concerns about what kind of keyboard a user is typing on, it will also make your game flexible to whatever is _most comfortable_ for a user. This is not just a question of keyboard layouts, but being kind to those that don't have full motion of their hands and would benefit from moving keys to accessible locations that don't make obvious sense to an outside observer. At least offer a config file, if not a user interface; people you've never met will thank you for it!


## The four approaches

There are, as far as we can tell, four common ways that apps want to use keyboard input. Sometimes they want different approaches at different moments, too.


## The 101-Button Joystick

Many games just want to treat a keyboard not as a way to input text, but just as a joystick that has a _lot_ of buttons. The well-known ["WASD" key pattern](https://en.wikipedia.org/wiki/WASD_keys) for FPS games is a fine example of this: you want the _physical_ location of a key, regardless of what symbol is printed on the key. After all, on a French keyboard, instead of "WASD", you'd press "ZQSD", and on a Hiragana keyboard "てちとし". Same locations on the keyboard, totally different symbols.

For these, you want [SDL_Scancodes](SDL_Scancode): these are guaranteed to reference the physical location on the keyboard and not what is printed on it.

Specifically, they assume a US English QWERTY keyboard layout, no matter what the keyboard in use actually has at that location, but that's okay because here we just want physical location of the key, not its meaning.

Simply grab the `scancode` field from [SDL_EVENT_KEY_DOWN](SDL_EVENT_KEY_DOWN) and [SDL_EVENT_KEY_UP](SDL_EVENT_KEY_UP) events.

```c
/* returns 1 if moving forward with this keypress, -1 if moving backward, 0 if not moving. */
int direction_user_should_move(const SDL_Event *e)
{
    SDL_assert(e->type == SDL_EVENT_KEY_DOWN); /* just checking key presses here... */
    if (e->key.scancode == SDL_SCANCODE_W) {
        return 1;  /* pressed what would be "W" on a US QWERTY keyboard. Move forward! */
    } else if (e->key.scancode == SDL_SCANCODE_S) {
        return -1;  /* pressed what would be "S" on a US QWERTY keyboard. Move backward! */
    }

    return 0;  /* wasn't key in W or S location, don't move. */
}
```


## The Specific Key

Some games might want to know the _symbol_ on a key. This tends to be a "press 'I' to open your inventory" thing, and you don't really care _where_ the 'I' key is on the keyboard.

(But, again: offer keybindings, because some keyboards don't _have_ an 'I' key!)

This is also useful for looking for the ESC key to cancel an operation, or Enter to confirm, etc; it doesn't matter where the key is, you still want _that_ key.

These are [SDL_Keycodes](SDL_Keycode). They name specific keys and don't care _where_ on the user's keyboard they actually are. Like scancodes, you also get these from [SDL_EVENT_KEY_DOWN](SDL_EVENT_KEY_DOWN) and [SDL_EVENT_KEY_UP](SDL_EVENT_KEY_UP) events.


```c
/* sit in a loop forever until the user presses Escape. */
SDL_bool quit_the_app = SDL_FALSE;
while (!quit_the_app) {
    SDL_Event e;
    while (SDL_WaitEvent(&e)) {
        /* user has pressed a key? */
        if (e.type == SDL_EVENT_KEY_DOWN) {
            /* the pressed key was Escape? */
            if (e.key.key == SDLK_ESCAPE) {
                quit_the_app = SDL_TRUE;
            }
        }
    }
}
```


## The Chat Box

Unicode is hard! If you are composing text a string at a time ("Enter your name, adventurer!" screens or accepting sentences for a chat interface, etc) you should _not_ be using key press events! This will _never_ do the right thing various keyboards and human languages around the world.

One should instead call [SDL_StartTextInput](SDL_StartTextInput), and listen for [SDL_EVENT_TEXT_INPUT](SDL_EVENT_TEXT_INPUT) events. When done accepting input, call [SDL_StopTextInput](SDL_StopTextInput). This approach will let the system provide input interfaces that are familiar to the user (including popping up a virtual keyboard on mobile devices, and other UI for composing in various languages). Then the event will provide Unicode strings in UTF-8 format, which might be complete lines of text or a single character, depending on the system. **You will not be able to replicate these interfaces in your application for everyone in the world**, do not try to build this yourself on top of individual keypress events.

The downside of this is that a virtual keyboard, etc, might be disruptive to your game, so you need to design accordingly.

```c
while (!quit_the_app) {
    /* Set the text area and start text input */
    char text[1024] = { 0 };
    SDL_Rect area = { textfield.x, textfield.y, textfield.w, textfield.h };
    int cursor = 0;
    SDL_SetTextInputArea(window, &area, cursor);
    SDL_StartTextInput(window);

    SDL_Event e;
    while (SDL_PollEvent(&e)) {
        /* user has pressed a key? */
        if (e.type == SDL_EVENT_KEY_DOWN) {
            /* the pressed key was Escape? */
            if (e.key.key == SDLK_ESCAPE) {
                SDL_StopTextInput(window);
            }
            /* Handle arrow keys, etc. */
        } else if (e.type == SDL_EVENT_TEXT_INPUT) {
            SDL_strlcat(text, e.text.text, sizeof(text));
        }
    }

    /* Render the text, adjusting cursor to the offset in pixels from the left edge of the textfield */
    ...

    /* Update the text input area, adjusting the cursor so IME UI shows up at the correct location. */
    SDL_SetTextInputArea(window, &area, cursor);
}
```

If you're writing a fullscreen game, you might want to render IME UI yourself, so you'd set SDL_HINT_IME_IMPLEMENTED_UI appropriately and handle the SDL_EVENT_TEXT_EDITING and SDL_EVENT_TEXT_EDITING_CANDIDATES events. See testime.c for an example of this.

## The Text Editor

This is a special case, and if you think your game fits here, you should think very hard about how to change that before thinking about how to go this route, because often times you are just on a path to build [The Chat Box](#the-chat-box), incorrectly, from scratch.

If you were writing an SDL frontend for [Vim](https://www.vim.org/), you would need to know what keypresses-plus-modifiers produce: hitting shift-Z twice produces a different result than pressing z twice, but also you want arrow keys to do the right thing on the numpad, unless NumLock is pressed, when they should produce numbers. On top of all this, it's difficult to correlate between keypress and proper text input events and untangle them to get correct results.

In this case, you would need to handle both key events and input events as above, in addition you might want to know what the modified keycode for the event is:

```c
while (!quit_the_app) {
    SDL_Event e;
    while (SDL_WaitEvent(&e)) {
        /* user has pressed a key? */
        if (e.type == SDL_EVENT_KEY_DOWN) {
            /* the pressed key was '$', generated by Shift+4 on a US keyboard and the '$' key on the French keyboard. */
            SDL_Keycode keycode = SDL_GetKeyFromScancode(e.key.scancode, e.key.mod);
            if (keycode == '$') {
                /* Show me the money! */
            }
        }
    }
}
```

Obviously there are many keys that _don't_ generate a character, or characters that are composed by pressing multiple keys (or navigating through IME interfaces that don't map to specific keypresses at all), so this is niche functionality and not how one should accept input in a general sense.


## Showing key names to users

So you've made your game, and now you're taking the original advice about adding user-configurable keybindings, and you need to know how to show the user the key's name in your config UI, and maybe also in a "press [current keybinding] to jump" tutorial message.
