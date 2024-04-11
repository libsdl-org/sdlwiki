###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowKeyboardGrab

Get a window's keyboard grab mode.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_bool SDL_GetWindowKeyboardGrab(SDL_Window * window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if keyboard is grabbed, and
[SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 2.0.16.

## See Also

* [SDL_SetWindowKeyboardGrab](SDL_SetWindowKeyboardGrab)
* [SDL_GetWindowGrab](SDL_GetWindowGrab)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

