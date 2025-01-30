###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetGlyphImageForIndex

Get the pixel image for a character index.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_Surface * TTF_GetGlyphImageForIndex(TTF_Font *font, Uint32 glyph_index, TTF_ImageType *image_type);
```

## Function Parameters

|                                  |                 |                                                             |
| -------------------------------- | --------------- | ----------------------------------------------------------- |
| [TTF_Font](TTF_Font) *           | **font**        | the font to query.                                          |
| Uint32                           | **glyph_index** | the index of the glyph to return.                           |
| [TTF_ImageType](TTF_ImageType) * | **image_type**  | a pointer filled in with the glyph image type, may be NULL. |

## Return Value

(SDL_Surface *) Returns an SDL_Surface containing the glyph, or NULL on
failure; call SDL_GetError() for more information.

## Remarks

This is useful for text engine implementations, which can call this with
the `glyph_index` in a [TTF_CopyOperation](TTF_CopyOperation)

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

