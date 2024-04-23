###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UpdateWindowSurfaceRects

Copy areas of the window surface to the screen.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

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

Note that this function will update _at least_ the rectangles specified,
but this is only intended as an optimization; in practice, this might
update more of the screen (or all of the screen!), depending on what method
SDL uses to send pixels to the system.

## Version

This function is available since SDL 2.0.0.

## See Also

* [SDL_GetWindowSurface](SDL_GetWindowSurface)
* [SDL_UpdateWindowSurface](SDL_UpdateWindowSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

