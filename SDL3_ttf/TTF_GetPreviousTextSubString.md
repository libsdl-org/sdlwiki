###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetPreviousTextSubString

Get the previous substring in a text object

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetPreviousTextSubString(TTF_Text *text, const TTF_SubString *substring, TTF_SubString *previous);
```

## Function Parameters

|                                        |               |                                                                     |
| -------------------------------------- | ------------- | ------------------------------------------------------------------- |
| [TTF_Text](TTF_Text) *                 | **text**      | the [TTF_Text](TTF_Text) to query.                                  |
| const [TTF_SubString](TTF_SubString) * | **substring** | the [TTF_SubString](TTF_SubString) to query.                        |
| [TTF_SubString](TTF_SubString) *       | **previous**  | a pointer filled in with the previous substring in the text object. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If called at the start of the text, this will return a zero length
substring with the [TTF_SUBSTRING_TEXT_START](TTF_SUBSTRING_TEXT_START)
flag set.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

