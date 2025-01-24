# SDL_GetWindowSurface

Get the SDL surface associated with the window.

## Header File

Defined in [<SDL3/SDL_video.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_video.h)

## Syntax

```c
SDL_Surface * SDL_GetWindowSurface(SDL_Window *window);
```

## Function Parameters

|                            |            |                      |
| -------------------------- | ---------- | -------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to query. |

## Return Value

([SDL_Surface](SDL_Surface) *) Returns the surface associated with the
window, or NULL on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

A new surface will be created with the optimal format for the window, if
necessary. This surface will be freed when the window is destroyed. Do not
free this surface.

This surface will be invalidated if the window is resized. After resizing a
window this function must be called again to return a valid surface.

You may not combine this with 3D or the rendering API on this window.

This function is affected by
[`SDL_HINT_FRAMEBUFFER_ACCELERATION`](SDL_HINT_FRAMEBUFFER_ACCELERATION).

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_DestroyWindowSurface](SDL_DestroyWindowSurface)
- [SDL_WindowHasSurface](SDL_WindowHasSurface)
- [SDL_UpdateWindowSurface](SDL_UpdateWindowSurface)
- [SDL_UpdateWindowSurfaceRects](SDL_UpdateWindowSurfaceRects)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

