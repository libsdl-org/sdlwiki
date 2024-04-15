###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!
# SDL_GetKeyboardFocus

Query the window which currently has keyboard focus.

## Header File

Defined in [SDL_keyboard.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_keyboard.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
SDL_Window * SDL_GetKeyboardFocus(void);

```

## Return Value

Returns the window with keyboard focus.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryKeyboard](CategoryKeyboard), [CategoryDraft](CategoryDraft)


