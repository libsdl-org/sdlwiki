# SDL_MUSTLOCK

Evaluates to true if the surface needs to be locked before access.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
#define SDL_MUSTLOCK(S) (((S)->flags & SDL_RLEACCEL) != 0)
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategorySurface](CategorySurface)

