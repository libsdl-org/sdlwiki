###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextSubString

Get the substring of a text object that surrounds a text offset.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetTextSubString(TTF_Text *text, int offset, TTF_SubString *substring);
```

## Function Parameters

|                                  |               |                                                               |
| -------------------------------- | ------------- | ------------------------------------------------------------- |
| [TTF_Text](TTF_Text) *           | **text**      | the [TTF_Text](TTF_Text) to query.                            |
| int                              | **offset**    | a byte offset into the text string.                           |
| [TTF_SubString](TTF_SubString) * | **substring** | a pointer filled in with the substring containing the offset. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If `offset` is less than 0, this will return a zero length substring at the
beginning of the text with the
[TTF_SUBSTRING_TEXT_START](TTF_SUBSTRING_TEXT_START) flag set. If `offset`
is greater than or equal to the length of the text string, this will return
a zero length substring at the end of the text with the
[TTF_SUBSTRING_TEXT_END](TTF_SUBSTRING_TEXT_END) flag set.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

