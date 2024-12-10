###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetTextPosition

Set the position of a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetTextPosition(TTF_Text *text, int x, int y);
```

## Function Parameters

|                        |          |                                                               |
| ---------------------- | -------- | ------------------------------------------------------------- |
| [TTF_Text](TTF_Text) * | **text** | the [TTF_Text](TTF_Text) to modify.                           |
| int                    | **x**    | the x offset of the upper left corner of this text in pixels. |
| int                    | **y**    | the y offset of the upper left corner of this text in pixels. |

## Remarks

This can be used to position multiple text objects within a single wrapping
text area.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetTextPosition](TTF_GetTextPosition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

