###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetGlyphMetrics

Query the metrics (dimensions) of a font's 32-bit glyph.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetGlyphMetrics(TTF_Font *font, Uint32 ch, int *minx, int *maxx, int *miny, int *maxy, int *advance);
```

## Function Parameters

|                        |             |                                                                                                                                      |
| ---------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| [TTF_Font](TTF_Font) * | **font**    | the font to query.                                                                                                                   |
| Uint32                 | **ch**      | the character code to check.                                                                                                         |
| int *                  | **minx**    | a pointer filled in with the minimum x coordinate of the glyph from the left edge of its bounding box. This value may be negative.   |
| int *                  | **maxx**    | a pointer filled in with the maximum x coordinate of the glyph from the left edge of its bounding box.                               |
| int *                  | **miny**    | a pointer filled in with the minimum y coordinate of the glyph from the bottom edge of its bounding box. This value may be negative. |
| int *                  | **maxy**    | a pointer filled in with the maximum y coordinate of the glyph from the bottom edge of its bounding box.                             |
| int *                  | **advance** | a pointer filled in with the distance to the next glyph from the left edge of this glyph's bounding box.                             |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

To understand what these metrics mean, here is a useful link:

https://freetype.sourceforge.net/freetype2/docs/tutorial/step2.html

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

