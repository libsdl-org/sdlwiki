###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ColorType

The color type

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
typedef enum SDL_ColorType
{
    SDL_COLOR_TYPE_UNKNOWN = 0,
    SDL_COLOR_TYPE_RGB = 1,
    SDL_COLOR_TYPE_YCBCR = 2
} SDL_ColorType;
```

## Version

This enum is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum)

