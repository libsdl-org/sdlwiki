###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetTextPosition

Get the position of a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_GetTextPosition(TTF_Text *text, int *x, int *y);
```

## Function Parameters

|                        |          |                                                                                                     |
| ---------------------- | -------- | --------------------------------------------------------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text** | the [TTF_Text](TTF_Text) to query.                                                                  |
| int *                  | **x**    | a pointer filled in with the x offset of the upper left corner of this text in pixels, may be NULL. |
| int *                  | **y**    | a pointer filled in with the y offset of the upper left corner of this text in pixels, may be NULL. |

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetTextPosition](TTF_SetTextPosition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

