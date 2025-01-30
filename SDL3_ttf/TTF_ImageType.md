###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_ImageType

The type of data in a glyph image

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
typedef enum TTF_ImageType
{
    TTF_IMAGE_INVALID,
    TTF_IMAGE_ALPHA,    /**< The color channels are white */
    TTF_IMAGE_COLOR,    /**< The color channels have image data */
    TTF_IMAGE_SDF,      /**< The alpha channel has signed distance field information */
} TTF_ImageType;
```

## Version

This enum is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySDLTTF](CategorySDLTTF)

