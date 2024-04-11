###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RendererFlags

Flags used when creating a rendering context.

## Header File

Defined in [SDL_render.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
typedef enum SDL_RendererFlags
{
    SDL_RENDERER_PRESENTVSYNC = 0x00000004  /**< Present is synchronized with the refresh rate */
} SDL_RendererFlags;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

