###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowSurface

Get the SDL surface associated with the window.

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
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

A new surface will be created with the optimal format for the window, if
necessary. This surface will be freed when the window is destroyed. Do not
free this surface.

This surface will be invalidated if the window is resized. After resizing a
window this function must be called again to return a valid surface.

You may not combine this with 3D or the rendering API on this window.

This function is affected by
[`SDL_HINT_FRAMEBUFFER_ACCELERATION`](SDL_HINT_FRAMEBUFFER_ACCELERATION).

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_DestroyWindowSurface](SDL_DestroyWindowSurface.md)
* [SDL_HasWindowSurface](SDL_HasWindowSurface.md)
* [SDL_UpdateWindowSurface](SDL_UpdateWindowSurface.md)
* [SDL_UpdateWindowSurfaceRects](SDL_UpdateWindowSurfaceRects.md)

----
[CategoryAPI](CategoryAPI.md)
