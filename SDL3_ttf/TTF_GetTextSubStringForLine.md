###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextSubStringForLine

Get the substring of a text object that contains the given line.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetTextSubStringForLine(TTF_Text *text, int line, TTF_SubString *substring);
```

## Function Parameters

|                                  |               |                                                                 |
| -------------------------------- | ------------- | --------------------------------------------------------------- |
| [TTF_Text](TTF_Text) *           | **text**      | the [TTF_Text](TTF_Text) to query.                              |
| int                              | **line**      | a zero-based line index, in the range [0 .. text->num_lines-1]. |
| [TTF_SubString](TTF_SubString) * | **substring** | a pointer filled in with the substring containing the offset.   |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

If `line` is less than 0, this will return a zero width substring at the
beginning of the text. If `line` is greater than or equal to
`text->num_lines` this will return a zero width substring at the end of the
text.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

