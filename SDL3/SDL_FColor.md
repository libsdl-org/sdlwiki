# SDL_FColor

The bits of this structure can be directly reinterpreted as a float-packed color which uses the [SDL_PIXELFORMAT_RGBA128_FLOAT](SDL_PIXELFORMAT_RGBA128_FLOAT) format

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
typedef struct SDL_FColor
{
    float r;
    float g;
    float b;
    float a;
} SDL_FColor;
```

## Version

This struct is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryPixels](CategoryPixels)

