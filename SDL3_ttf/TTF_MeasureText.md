###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_MeasureText

Calculate how much of a UTF-8 string will fit in a given width.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_MeasureText(TTF_Font *font, const char *text, size_t length, int measure_width, int *extent, int *count);
```

## Function Parameters

|                        |                   |                                                                   |
| ---------------------- | ----------------- | ----------------------------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**          | the font to query.                                                |
| const char *           | **text**          | text to calculate, in UTF-8 encoding.                             |
| size_t                 | **length**        | the length of the text, in bytes, or 0 for null terminated text.  |
| int                    | **measure_width** | maximum width, in pixels, available for the string.               |
| int *                  | **extent**        | on return, filled with latest calculated width.                   |
| int *                  | **count**         | on return, filled with number of characters that can be rendered. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This reports the number of characters that can be rendered before reaching
`measure_width`.

This does not need to render the string to do this calculation.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

