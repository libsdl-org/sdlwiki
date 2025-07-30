# SDL_ScaleMode

The scaling mode.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
typedef enum SDL_ScaleMode
{
    SDL_SCALEMODE_INVALID = -1,
    SDL_SCALEMODE_NEAREST,  /**< nearest pixel sampling */
    SDL_SCALEMODE_LINEAR,   /**< linear filtering */
    SDL_SCALEMODE_PIXELART  /**< nearest pixel sampling with improved scaling for pixel art */
} SDL_ScaleMode;
```

## Version

This enum is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySurface](CategorySurface)

