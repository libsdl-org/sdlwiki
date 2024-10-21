###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextWrapWidth

Get whether wrapping is enabled on a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetTextWrapWidth(TTF_Text *text, int *wrap_width);
```

## Function Parameters

|                        |                |                                                                                                               |
| ---------------------- | -------------- | ------------------------------------------------------------------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text**       | the [TTF_Text](TTF_Text) to query.                                                                            |
| int *                  | **wrap_width** | a pointer filled in with the maximum width in pixels or 0 if the text is being wrapped on newline characters. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetTextWrapWidth](TTF_SetTextWrapWidth)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

