###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowInputFocus

Explicitly set input focus to the window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_SetWindowInputFocus(SDL_Window * window);

```

## Function Parameters

|                |                                            |
| -------------- | ------------------------------------------ |
| **window**     | the window that should get the input focus |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

You almost certainly want [SDL_RaiseWindow](SDL_RaiseWindow)() instead of
this function. Use this with caution, as you might give focus to a window
that is completely obscured by other windows.

## Version

This function is available since SDL 2.0.5.

## Related Functions

* [SDL_RaiseWindow](SDL_RaiseWindow)

----
[CategoryAPI](CategoryAPI)

