###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextColorFloat

Get the color of a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetTextColorFloat(TTF_Text *text, float *r, float *g, float *b, float *a);
```

## Function Parameters

|                        |          |                                                                                            |
| ---------------------- | -------- | ------------------------------------------------------------------------------------------ |
| [TTF_Text](TTF_Text) * | **text** | the [TTF_Text](TTF_Text) to query.                                                         |
| float *                | **r**    | a pointer filled in with the red color value, normally in the range of 0-1, may be NULL.   |
| float *                | **g**    | a pointer filled in with the green color value, normally in the range of 0-1, may be NULL. |
| float *                | **b**    | a pointer filled in with the blue color value, normally in the range of 0-1, may be NULL.  |
| float *                | **a**    | a pointer filled in with the alpha value in the range of 0-1, may be NULL.                 |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetTextColor](TTF_GetTextColor)
- [TTF_SetTextColorFloat](TTF_SetTextColorFloat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

