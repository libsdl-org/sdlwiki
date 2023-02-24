###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_UpdateWindowSurfaceRects

Copy areas of the window surface to the screen.

## Syntax

```c
int SDL_UpdateWindowSurfaceRects(SDL_Window *window, const SDL_Rect *rects, int numrects);

```

## Function Parameters

|                  |                                                                                                  |
| ---------------- | ------------------------------------------------------------------------------------------------ |
| **window**       | the window to update                                                                             |
| **rects**        | an array of [SDL_Rect](SDL_Rect) structures representing areas of the surface to copy, in pixels |
| **numrects**     | the number of rectangles                                                                         |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This is the function you use to reflect changes to portions of the surface
on the screen.

This function is equivalent to the SDL 1.2 API
[SDL_UpdateRects](SDL_UpdateRects)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetWindowSurface](SDL_GetWindowSurface)
* [SDL_UpdateWindowSurface](SDL_UpdateWindowSurface)

----
[CategoryAPI](CategoryAPI), [CategoryVideo](CategoryVideo)


