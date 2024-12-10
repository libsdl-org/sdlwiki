###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_TextWrapWhitespaceVisible

Return whether whitespace is shown when wrapping a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_TextWrapWhitespaceVisible(TTF_Text *text);
```

## Function Parameters

|                        |          |                                    |
| ---------------------- | -------- | ---------------------------------- |
| [TTF_Text](TTF_Text) * | **text** | the [TTF_Text](TTF_Text) to query. |

## Return Value

(bool) Returns true if whitespace is shown when wrapping text, or false
otherwise.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetTextWrapWhitespaceVisible](TTF_SetTextWrapWhitespaceVisible)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

