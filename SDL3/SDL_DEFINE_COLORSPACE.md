# SDL_DEFINE_COLORSPACE

A macro for defining custom [SDL_Colorspace](SDL_Colorspace) formats.

## Header File

Defined in [<SDL3/SDL_pixels.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_pixels.h)

## Syntax

```c
#define SDL_DEFINE_COLORSPACE(type, range, primaries, transfer, matrix, chroma) \
    (((Uint32)(type) << 28) | ((Uint32)(range) << 24) | ((Uint32)(chroma) << 20) | \
    ((Uint32)(primaries) << 10) | ((Uint32)(transfer) << 5) | ((Uint32)(matrix) << 0))
```

## Macro Parameters

|               |                                                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| **type**      | the type of the new format, probably an [SDL_ColorType](SDL_ColorType) value.                                                 |
| **range**     | the range of the new format, probably a [SDL_ColorRange](SDL_ColorRange) value.                                               |
| **primaries** | the primaries of the new format, probably an [SDL_ColorPrimaries](SDL_ColorPrimaries) value.                                  |
| **transfer**  | the transfer characteristics of the new format, probably an [SDL_TransferCharacteristics](SDL_TransferCharacteristics) value. |
| **matrix**    | the matrix coefficients of the new format, probably an [SDL_MatrixCoefficients](SDL_MatrixCoefficients) value.                |
| **chroma**    | the chroma sample location of the new format, probably an [SDL_ChromaLocation](SDL_ChromaLocation) value.                     |

## Return Value

Returns a format value in the style of [SDL_Colorspace](SDL_Colorspace).

## Remarks

For example, defining [SDL_COLORSPACE_SRGB](SDL_COLORSPACE_SRGB) looks like
this:

```c
SDL_DEFINE_COLORSPACE(SDL_COLOR_TYPE_RGB,
                      SDL_COLOR_RANGE_FULL,
                      SDL_COLOR_PRIMARIES_BT709,
                      SDL_TRANSFER_CHARACTERISTICS_SRGB,
                      SDL_MATRIX_COEFFICIENTS_IDENTITY,
                      SDL_CHROMA_LOCATION_NONE)
```

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryPixels](CategoryPixels)

