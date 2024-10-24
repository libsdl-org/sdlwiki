###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ScaleMode

The scaling mode.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
typedef enum SDL_ScaleMode
{
    SDL_SCALEMODE_NEAREST, /**< nearest pixel sampling */
    SDL_SCALEMODE_LINEAR   /**< linear filtering */
} SDL_ScaleMode;
```

## Version

This enum is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySurface](CategorySurface)

