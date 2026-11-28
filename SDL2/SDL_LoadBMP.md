# SDL_LoadBMP

Load a BMP image from a file.

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_surface.h)

## Syntax

```c
#define SDL_LoadBMP(file)   SDL_LoadBMP_RW(SDL_RWFromFile(file, "rb"), 1)
```

## Remarks

This is designed as a convenience function for loading images from trusted
sources. Crashes or other issues with invalid content should not be
considered security issues. If you want to load arbitrary images you should
use an image loading library designed with security in mind.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategorySurface](CategorySurface)

