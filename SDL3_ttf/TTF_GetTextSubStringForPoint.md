###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextSubStringForPoint

Get the portion of a text string that is closest to a point.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetTextSubStringForPoint(TTF_Text *text, int x, int y, TTF_SubString *substring);
```

## Function Parameters

|                                  |               |                                                                                                     |
| -------------------------------- | ------------- | --------------------------------------------------------------------------------------------------- |
| [TTF_Text](TTF_Text) *           | **text**      | the [TTF_Text](TTF_Text) to query.                                                                  |
| int                              | **x**         | the x coordinate relative to the left side of the text, may be outside the bounds of the text area. |
| int                              | **y**         | the y coordinate relative to the top side of the text, may be outside the bounds of the text area.  |
| [TTF_SubString](TTF_SubString) * | **substring** | a pointer filled in with the closest substring of text to the given point.                          |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

This will return the closest substring of text to the given point.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

