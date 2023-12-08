###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_DestroyWindowSurface

Destroy the surface associated with the window.

## Syntax

```c
int SDL_DestroyWindowSurface(SDL_Window *window);

```

## Function Parameters

|                |                      |
| -------------- | -------------------- |
| **window**     | the window to update |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Version

This function is available since SDL 2.28.0.

## Related Functions

* [SDL_GetWindowSurface](SDL_GetWindowSurface.md)
* [SDL_HasWindowSurface](SDL_HasWindowSurface.md)

----
[CategoryAPI](CategoryAPI.md)
