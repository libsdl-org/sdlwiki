###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetTextWrapWhitespaceVisible

Set whether whitespace should be visible when wrapping a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetTextWrapWhitespaceVisible(TTF_Text *text, bool visible);
```

## Function Parameters

|                        |             |                                                               |
| ---------------------- | ----------- | ------------------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text**    | the [TTF_Text](TTF_Text) to modify.                           |
| bool                   | **visible** | true to show whitespace when wrapping text, false to hide it. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If the whitespace is visible, it will take up space for purposes of
alignment and wrapping. This is good for editing, but looks better when
centered or aligned if whitespace around line wrapping is hidden. This
defaults false.

This function may cause the internal text representation to be rebuilt.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_TextWrapWhitespaceVisible](TTF_TextWrapWhitespaceVisible)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

