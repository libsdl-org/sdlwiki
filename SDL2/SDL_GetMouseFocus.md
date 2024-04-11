###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetMouseFocus

Get the window which currently has mouse focus.

## Header File

Defined in [SDL_mouse.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mouse.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_Window * SDL_GetMouseFocus(void);

```

## Return Value

Returns the window with mouse focus.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

