###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetStringSizeWrapped

Calculate the dimensions of a rendered string of UTF-8 text.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetStringSizeWrapped(TTF_Font *font, const char *text, size_t length, int wrapLength, int *w, int *h);
```

## Function Parameters

|                        |                |                                                                  |
| ---------------------- | -------------- | ---------------------------------------------------------------- |
| [TTF_Font](TTF_Font) * | **font**       | the font to query.                                               |
| const char *           | **text**       | text to calculate, in UTF-8 encoding.                            |
| size_t                 | **length**     | the length of the text, in bytes, or 0 for null terminated text. |
| int                    | **wrapLength** | the maximum width or 0 to wrap on newline characters.            |
| int *                  | **w**          | will be filled with width, in pixels, on return.                 |
| int *                  | **h**          | will be filled with height, in pixels, on return.                |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This will report the width and height, in pixels, of the space that the
specified string will take to fully render.

Text is wrapped to multiple lines on line endings and on word boundaries if
it extends beyond `wrapLength` in pixels.

If wrapLength is 0, this function will only wrap on newline characters.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

