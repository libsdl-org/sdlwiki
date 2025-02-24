# SDL_StartTextInput

Start accepting Unicode text input events.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_keyboard.h)

## Syntax

```c
void SDL_StartTextInput(void);
```

## Remarks

This function will start accepting Unicode text input events in the focused
SDL window, and start emitting [SDL_TextInputEvent](SDL_TextInputEvent)
([SDL_TEXTINPUT](SDL_TEXTINPUT)) and
[SDL_TextEditingEvent](SDL_TextEditingEvent)
([SDL_TEXTEDITING](SDL_TEXTEDITING)) events. Please use this function in
pair with [SDL_StopTextInput](SDL_StopTextInput)().

On some platforms using this function activates the screen keyboard.

On desktop platforms, [SDL_StartTextInput](SDL_StartTextInput)() is
implicitly called on SDL video subsystem initialization which will cause
[SDL_TextInputEvent](SDL_TextInputEvent) and
[SDL_TextEditingEvent](SDL_TextEditingEvent) to begin emitting.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_SetTextInputRect](SDL_SetTextInputRect)
- [SDL_StopTextInput](SDL_StopTextInput)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard)

