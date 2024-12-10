###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontSize

Get the size of a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
float TTF_GetFontSize(TTF_Font *font);
```

## Function Parameters

|                        |          |                    |
| ---------------------- | -------- | ------------------ |
| [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(float) Returns the size of the font, or 0.0f on failure; call
SDL_GetError() for more information.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetFontSize](TTF_SetFontSize)
- [TTF_SetFontSizeDPI](TTF_SetFontSizeDPI)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

