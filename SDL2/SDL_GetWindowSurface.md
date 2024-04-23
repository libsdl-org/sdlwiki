###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowSurface

Get the SDL surface associated with the window.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
SDL_Surface * SDL_GetWindowSurface(SDL_Window * window);

```

## Function Parameters

|                |                     |
| -------------- | ------------------- |
| **window**     | the window to query |

## Return Value

Returns the surface associated with the window, or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

A new surface will be created with the optimal format for the window, if
necessary. This surface will be freed when the window is destroyed. Do not
free this surface.

This surface will be invalidated if the window is resized. After resizing a
window this function must be called again to return a valid surface.

Note that on some platforms the pixels pointer of the surface may be
modified after each call to
[SDL_UpdateWindowSurface](SDL_UpdateWindowSurface)(), so that the platform
code can implement efficient double or triple buffering.

You may not combine this with 3D or the rendering API on this window.

This function is affected by
[`SDL_HINT_FRAMEBUFFER_ACCELERATION`](SDL_HINT_FRAMEBUFFER_ACCELERATION).

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_DestroyWindowSurface](SDL_DestroyWindowSurface)
* [SDL_HasWindowSurface](SDL_HasWindowSurface)
* [SDL_UpdateWindowSurface](SDL_UpdateWindowSurface)
* [SDL_UpdateWindowSurfaceRects](SDL_UpdateWindowSurfaceRects)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

