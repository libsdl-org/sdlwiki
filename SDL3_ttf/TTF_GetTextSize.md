###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextSize

Get the size of a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetTextSize(TTF_Text *text, int *w, int *h);
```

## Function Parameters

|                        |          |                                                                          |
| ---------------------- | -------- | ------------------------------------------------------------------------ |
| [TTF_Text](TTF_Text) * | **text** | the [TTF_Text](TTF_Text) to query.                                       |
| int *                  | **w**    | a pointer filled in with the width of the text, in pixels, may be NULL.  |
| int *                  | **h**    | a pointer filled in with the height of the text, in pixels, may be NULL. |

## Return Value

(bool) Returns true on success or false on failure; call SDL_GetError() for
more information.

## Remarks

The size of the text may change when the font or font style and size
change.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

