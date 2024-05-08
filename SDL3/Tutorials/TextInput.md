# Text Input

## Why?

Why does SDL need a text input API?

When I press a key on my keyboard, my program receives a character event, right?

Well, it's not always that simple. Sometimes it can take multiple key presses to produce a character. Sometimes a single key press can produce multiple characters.

Text input is not as simple as it seems, particularly when you consider International users (and you should). It's not hard to figure out why that is when you look at languages like Chinese, Japanese, and Korean. These languages, collectively referred to as the CJK, have thousands of symbols.

It would not be feasible to have a keyboard with over ten-thousand keys, would it? The solution to this is a software input method.

## Terms

- **IME** - Input Method Editor. A software input method. This is typically a program that intercepts key presses and interprets them before (eventually) passing them onto the application.
- **Composition** - The text a user is currently inputting. This text is not yet finalized (committed) and the IME may modify it. Conventionally, this text is drawn with a solid or dotted line under it.
- **Candidate** - An optional alternative text for the composition, gathered by the IME in the Candidate List.
- **Candidate List** - A list of Candidates, used when there is any ambiguity.

## Workflow

1. The user activates an input method IME. This is typically done via a hotkey or by selecting an input method in a GUI.
2. The user begins to type in their selected language, starting a Composition.
3. The user continues typing until the composition is satisfactory.
4. Alternatively, the user may choose to open the Candidate List and select a Candidate. The IME can also force the Candidate List to open.
5. The user commits the Composition, terminating it. The IME passes the text onto the application.

While this provides a good overview, it may not be accurate for all platforms.

There are multiple input method styles which you can read about [here](http://www-archive.mozilla.org/projects/intl/input-method-spec.html). SDL supports "on-the-spot" mode. This has an important implication: the application is responsible for drawing the composition.

## SDL

So how does SDL handle text input?

First, an example:

### Example

```c
#include "SDL.h"

extern void InitVideo();
extern void Redraw();

extern char *text;
extern char *composition;
extern Sint32 cursor;
extern Sint32 selection_len;

int main(int argc, char *argv[])
{
    SDL_bool done = SDL_FALSE;

    InitVideo();
    /* ... */

    SDL_StartTextInput();
    while (!done) {
        SDL_Event event;
        if (SDL_PollEvent(&event)) {
            switch (event.type) {
                case SDL_EVENT_QUIT:
                    /* Quit */
                    done = SDL_TRUE;
                    break;
                case SDL_EVENT_TEXT_INPUT:
                    /* Add new text onto the end of our text */
                    strcat(text, event.text.text);
                    break;
                case SDL_EVENT_TEXT_EDITING:
                    /*
                    Update the composition text.
                    Update the cursor position.
                    Update the selection length (if any).
                    */
                    composition = event.edit.text;
                    cursor = event.edit.start;
                    selection_len = event.edit.length;
                    break;
            }
        }
        Redraw();
    }

    SDL_Quit();

    return 0;
}
```

### Functions

- [SDL_StartTextInput](SDL_StartTextInput)
- [SDL_StopTextInput](SDL_StopTextInput)
- [SDL_SetTextInputRect](SDL_SetTextInputRect)
- [SDL_TextInputActive](SDL_TextInputActive)
- [SDL_ScreenKeyboardShown](SDL_ScreenKeyboardShown)
- [SDL_HasScreenKeyboardSupport](SDL_HasScreenKeyboardSupport)

### Events

- [SDL_TextEditingEvent](SDL_TextEditingEvent)
- [SDL_TextInputEvent](SDL_TextInputEvent)

One important thing to notice is that the application can enable and disable text input arbitrarily with [SDL_StartTextInput](SDL_StartTextInput)() and [SDL_StopTextInput](SDL_StopTextInput)(). [SDL_SetTextInputRect](SDL_SetTextInputRect)() controls where the Candidate List will open, if supported.

The application will receive an [SDL_TextEditingEvent](SDL_TextEditingEvent) when a composition is changed (or started). This event contains the composition text as well as the cursor position within the composition. It also contains a length member that determines the length of the text selection, if any.

The application will receive an [SDL_TextInputEvent](SDL_TextInputEvent) when a composition is committed and also for normal (non-IME) text input. Receiving this event implies that a composition has been committed or a composition never began (direct text input).
