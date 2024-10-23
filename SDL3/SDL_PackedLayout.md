###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_PackedLayout

Packed component layout.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
typedef enum SDL_PackedLayout
{
    SDL_PACKEDLAYOUT_NONE,
    SDL_PACKEDLAYOUT_332,
    SDL_PACKEDLAYOUT_4444,
    SDL_PACKEDLAYOUT_1555,
    SDL_PACKEDLAYOUT_5551,
    SDL_PACKEDLAYOUT_565,
    SDL_PACKEDLAYOUT_8888,
    SDL_PACKEDLAYOUT_2101010,
    SDL_PACKEDLAYOUT_1010102
} SDL_PackedLayout;
```

## Version

This enum is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryPixels](CategoryPixels)

