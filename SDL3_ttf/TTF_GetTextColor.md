###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextColor

Get the color of a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetTextColor(TTF_Text *text, Uint8 *r, Uint8 *g, Uint8 *b, Uint8 *a);
```

## Function Parameters

|                        |          |                                                                                    |
| ---------------------- | -------- | ---------------------------------------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text** | the [TTF_Text](TTF_Text) to query.                                                 |
| Uint8 *                | **r**    | a pointer filled in with the red color value in the range of 0-255, may be NULL.   |
| Uint8 *                | **g**    | a pointer filled in with the green color value in the range of 0-255, may be NULL. |
| Uint8 *                | **b**    | a pointer filled in with the blue color value in the range of 0-255, may be NULL.  |
| Uint8 *                | **a**    | a pointer filled in with the alpha value in the range of 0-255, may be NULL.       |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetTextColorFloat](TTF_GetTextColorFloat)
- [TTF_SetTextColor](TTF_SetTextColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

