###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_FlipMode

The flip mode.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
typedef enum SDL_FlipMode
{
    SDL_FLIP_NONE,          /**< Do not flip */
    SDL_FLIP_HORIZONTAL,    /**< flip horizontally */
    SDL_FLIP_VERTICAL       /**< flip vertically */
} SDL_FlipMode;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySurface](CategorySurface)

