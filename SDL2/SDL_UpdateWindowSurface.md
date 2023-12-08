###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_UpdateWindowSurface

Copy the window surface to the screen.

## Syntax

```c
int SDL_UpdateWindowSurface(SDL_Window * window);

```

## Function Parameters

|                |                      |
| -------------- | -------------------- |
| **window**     | the window to update |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This is the function you use to reflect any changes to the surface on the
screen.

This function is equivalent to the SDL 1.2 API [SDL_Flip](SDL_Flip.md)().

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowSurface](SDL_GetWindowSurface.md)
* [SDL_UpdateWindowSurfaceRects](SDL_UpdateWindowSurfaceRects.md)

----
[CategoryAPI](CategoryAPI.md)
