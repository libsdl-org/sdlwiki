###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UpdateWindowSurfaceRects

Copy areas of the window surface to the screen.

## Syntax

```c
int SDL_UpdateWindowSurfaceRects(SDL_Window * window,
                                 const SDL_Rect * rects,
                                 int numrects);

```

## Function Parameters

|                  |                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| **window**       | the window to update                                                                             |
| **rects**        | an array of [SDL_Rect](SDL_Rect.md) structures representing areas of the surface to copy, in pixels |
| **numrects**     | the number of rectangles                                                                         |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This is the function you use to reflect changes to portions of the surface
on the screen.

This function is equivalent to the SDL 1.2 API
[SDL_UpdateRects](SDL_UpdateRects.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowSurface](SDL_GetWindowSurface.md)
* [SDL_UpdateWindowSurface](SDL_UpdateWindowSurface.md)

----
[CategoryAPI](CategoryAPI.md)
