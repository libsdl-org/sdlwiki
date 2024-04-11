###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ScaleMode

The scaling mode

## Header File

Defined in [SDL_surface.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_surface.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef enum SDL_ScaleMode
{
    SDL_SCALEMODE_NEAREST, /**< nearest pixel sampling */
    SDL_SCALEMODE_LINEAR,  /**< linear filtering */
    SDL_SCALEMODE_BEST     /**< anisotropic filtering */
} SDL_ScaleMode;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

