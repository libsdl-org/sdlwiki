###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_StartTextInput

Start accepting Unicode text input events.

## Syntax

```c
void SDL_StartTextInput(void);

```

## Remarks

This function will start accepting Unicode text input events in the focused
SDL window, and start emitting [SDL_TextInputEvent](SDL_TextInputEvent.md)
([SDL_EVENT_TEXT_INPUT](SDL_EVENT_TEXT_INPUT.md)) and
[SDL_TextEditingEvent](SDL_TextEditingEvent.md)
([SDL_EVENT_TEXT_EDITING](SDL_EVENT_TEXT_EDITING.md)) events. Please use this
function in pair with [SDL_StopTextInput](SDL_StopTextInput.md)().

On some platforms using this function activates the screen keyboard.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SetTextInputRect](SDL_SetTextInputRect.md)
* [SDL_StopTextInput](SDL_StopTextInput.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryKeyboard](CategoryKeyboard.md), [CategoryDraft](CategoryDraft.md)
