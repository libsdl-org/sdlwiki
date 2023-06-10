###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasWindowSurface

Return whether the window has a surface associated with it.

## Syntax

```c
SDL_bool SDL_HasWindowSurface(SDL_Window *window);

```

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if there is a surface associated with the
window, or [SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 2.28.0.

## Related Functions

* [SDL_GetWindowSurface](SDL_GetWindowSurface)

----
[CategoryAPI](CategoryAPI)

