###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_StopTextInput

Stop receiving any text input events.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void SDL_StopTextInput(void);

```

## Remarks

Text input events are received by default.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_StartTextInput](SDL_StartTextInput)

----
[CategoryAPI](CategoryAPI), [CategoryKeyboard](CategoryKeyboard), [CategoryDraft](CategoryDraft)


