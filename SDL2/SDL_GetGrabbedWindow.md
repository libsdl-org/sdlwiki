###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetGrabbedWindow

Get the window that currently has an input grab enabled.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_Window * SDL_GetGrabbedWindow(void);

```

## Return Value

Returns the window if input is grabbed or NULL otherwise.

## Version

This function is available since SDL 2.0.4.

## See Also

* [SDL_GetWindowGrab](SDL_GetWindowGrab)
* [SDL_SetWindowGrab](SDL_SetWindowGrab)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

