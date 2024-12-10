###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetTextFont

Set the font used by a text object.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
bool TTF_SetTextFont(TTF_Text *text, TTF_Font *font);
```

## Function Parameters

|                        |          |                                     |
| ---------------------- | -------- | ----------------------------------- |
| [TTF_Text](TTF_Text) * | **text** | the [TTF_Text](TTF_Text) to modify. |
| [TTF_Font](TTF_Font) * | **font** | the font to use, may be NULL.       |

## Remarks

When a text object has a font, any changes to the font will automatically
regenerate the text. If you set the font to NULL, the text will continue to
render but changes to the font will no longer affect the text.

## Thread Safety

This function should be called on the thread that created the text.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_GetTextFont](TTF_GetTextFont)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

