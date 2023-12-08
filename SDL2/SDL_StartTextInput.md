###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_StartTextInput

Start accepting Unicode text input events.

## Syntax

```c
void SDL_StartTextInput(void);

```

## Remarks

This function will start accepting Unicode text input events in the focused
SDL window, and start emitting [SDL_TextInputEvent](SDL_TextInputEvent.md)
([SDL_TEXTINPUT](SDL_TEXTINPUT.md)) and
[SDL_TextEditingEvent](SDL_TextEditingEvent.md)
([SDL_TEXTEDITING](SDL_TEXTEDITING.md)) events. Please use this function in
pair with [SDL_StopTextInput](SDL_StopTextInput.md)().

On some platforms using this function activates the screen keyboard.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_SetTextInputRect](SDL_SetTextInputRect.md)
* [SDL_StopTextInput](SDL_StopTextInput.md)

----
[CategoryAPI](CategoryAPI.md)
