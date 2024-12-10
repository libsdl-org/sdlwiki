###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetTextColorFloat

Set the color of a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetTextColorFloat(TTF_Text *text, float r, float g, float b, float a);
```

## Function Parameters

|                        |          |                                                      |
| ---------------------- | -------- | ---------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text** | the [TTF_Text](TTF_Text) to modify.                  |
| float                  | **r**    | the red color value, normally in the range of 0-1.   |
| float                  | **g**    | the green color value, normally in the range of 0-1. |
| float                  | **b**    | the blue color value, normally in the range of 0-1.  |
| float                  | **a**    | the alpha value in the range of 0-1.                 |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

The default text color is white (1.0f, 1.0f, 1.0f, 1.0f).

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetTextColorFloat](TTF_GetTextColorFloat)
- [TTF_SetTextColor](TTF_SetTextColor)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

