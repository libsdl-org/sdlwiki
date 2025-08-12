###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontCharSpacing

Get the additional character spacing in pixels to be applied between any two rendered characters.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
int TTF_GetFontCharSpacing(TTF_Font *font);
```

## Function Parameters

|                        |          |                    |
| ---------------------- | -------- | ------------------ |
| [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

(int) Returns the character spacing in pixels.

## Remarks

This defaults to 0 if it hasn't been set.

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySDLTTF](CategorySDLTTF)

