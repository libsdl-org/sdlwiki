###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_blit

The type of function used for surface blitting functions.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
typedef int (SDLCALL *SDL_blit) (struct SDL_Surface * src, SDL_Rect * srcrect, struct SDL_Surface * dst, SDL_Rect * dstrect);
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype)

