###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetTextColor

Set the color of a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetTextColor(TTF_Text *text, Uint8 r, Uint8 g, Uint8 b, Uint8 a);
```

## Function Parameters

|                        |          |                                              |
| ---------------------- | -------- | -------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text** | the [TTF_Text](TTF_Text) to modify.          |
| Uint8                  | **r**    | the red color value in the range of 0-255.   |
| Uint8                  | **g**    | the green color value in the range of 0-255. |
| Uint8                  | **b**    | the blue color value in the range of 0-255.  |
| Uint8                  | **a**    | the alpha value in the range of 0-255.       |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

The default text color is white (255, 255, 255, 255).

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetTextColor](TTF_GetTextColor)
- [TTF_SetTextColorFloat](TTF_SetTextColorFloat)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

