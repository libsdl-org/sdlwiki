# SDL_FlipMode

The flip mode.

## Header File

Defined in [<SDL3/SDL_surface.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h)

## Syntax

```c
typedef enum SDL_FlipMode
{
    SDL_FLIP_NONE,                                                                  /**< Do not flip */
    SDL_FLIP_HORIZONTAL,                                                            /**< flip horizontally */
    SDL_FLIP_VERTICAL,                                                              /**< flip vertically */
    SDL_FLIP_HORIZONTAL_AND_VERTICAL = (SDL_FLIP_HORIZONTAL | SDL_FLIP_VERTICAL)    /**< flip horizontally and vertically (not a diagonal flip) */
} SDL_FlipMode;
```

## Version

This enum is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySurface](CategorySurface)

