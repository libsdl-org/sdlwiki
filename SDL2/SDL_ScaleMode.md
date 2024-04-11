###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_ScaleMode

The scaling mode for a texture.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_render.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
typedef enum SDL_ScaleMode
{
    SDL_ScaleModeNearest, /**< nearest pixel sampling */
    SDL_ScaleModeLinear,  /**< linear filtering */
    SDL_ScaleModeBest     /**< anisotropic filtering */
} SDL_ScaleMode;
```

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

