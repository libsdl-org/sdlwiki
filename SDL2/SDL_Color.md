###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Color

The bits of this structure can be directly reinterpreted as an integer-packed color which uses the [SDL_PIXELFORMAT_RGBA32](SDL_PIXELFORMAT_RGBA32) format ([SDL_PIXELFORMAT_ABGR8888](SDL_PIXELFORMAT_ABGR8888) on little-endian systems and [SDL_PIXELFORMAT_RGBA8888](SDL_PIXELFORMAT_RGBA8888) on big-endian systems).

## Header File

Defined in [SDL_pixels.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_pixels.h)

## Syntax

```c
typedef struct SDL_Color
{
    Uint8 r;
    Uint8 g;
    Uint8 b;
    Uint8 a;
} SDL_Color;
```

## Data Fields

{|
|Uint8
|'''r'''
|the red component in the range 0-255
|-
|Uint8
|'''g'''
|the green component in the range 0-255
|-
|Uint8
|'''b'''
|the blue component in the range 0-255
|-
|Uint8
|'''a'''
|the alpha component in the range 0-255
|}

## Related Structures

[SDL_Palette](SDL_Palette)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryStruct](CategoryStruct), [CategoryPixels](CategoryPixels)


