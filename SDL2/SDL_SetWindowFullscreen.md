###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowFullscreen

Set a window's fullscreen state.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_SetWindowFullscreen(SDL_Window * window,
                            Uint32 flags);

```

## Function Parameters

|                |                                                                                                                         |
| -------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **window**     | the window to change                                                                                                    |
| **flags**      | [`SDL_WINDOW_FULLSCREEN`](SDL_WINDOW_FULLSCREEN), [`SDL_WINDOW_FULLSCREEN_DESKTOP`](SDL_WINDOW_FULLSCREEN_DESKTOP) or 0 |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

`flags` may be [`SDL_WINDOW_FULLSCREEN`](SDL_WINDOW_FULLSCREEN), for "real"
fullscreen with a videomode change;
[`SDL_WINDOW_FULLSCREEN_DESKTOP`](SDL_WINDOW_FULLSCREEN_DESKTOP) for "fake"
fullscreen that takes the size of the desktop; and 0 for windowed mode.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowDisplayMode](SDL_GetWindowDisplayMode)
* [SDL_SetWindowDisplayMode](SDL_SetWindowDisplayMode)

----
[CategoryAPI](CategoryAPI)

