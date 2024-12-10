###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_MeasureString

Calculate how much of a UTF-8 string will fit in a given width.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_MeasureString(TTF_Font *font, const char *text, size_t length, int max_width, int *measured_width, size_t *measured_length);
```

## Function Parameters

|                        |                     |                                                                                          |
| ---------------------- | ------------------- | ---------------------------------------------------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**            | the font to query.                                                                       |
| const char *           | **text**            | text to calculate, in UTF-8 encoding.                                                    |
| size_t                 | **length**          | the length of the text, in bytes, or 0 for null terminated text.                         |
| int                    | **max_width**       | maximum width, in pixels, available for the string, or 0 for unbounded width.            |
| int *                  | **measured_width**  | a pointer filled in with the width, in pixels, of the string that will fit, may be NULL. |
| size_t *               | **measured_length** | a pointer filled in with the length, in bytes, of the string that will fit, may be NULL. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This reports the number of characters that can be rendered before reaching
`max_width`.

This does not need to render the string to do this calculation.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

