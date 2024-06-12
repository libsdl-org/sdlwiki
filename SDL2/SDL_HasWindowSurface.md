###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasWindowSurface

Return whether the window has a surface associated with it.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
SDL_bool SDL_HasWindowSurface(SDL_Window *window);
```

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if there is a surface
associated with the window, or [SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 2.28.0.

## See Also

- [SDL_GetWindowSurface](SDL_GetWindowSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

