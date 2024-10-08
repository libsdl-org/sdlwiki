###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_GetFontDirection

Get direction to be used for text shaping by a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
TTF_Direction TTF_GetFontDirection(TTF_Font *font);
```

## Function Parameters

|                        |          |                    |
| ---------------------- | -------- | ------------------ |
| [TTF_Font](TTF_Font) * | **font** | the font to query. |

## Return Value

([TTF_Direction](TTF_Direction)) Returns the direction to be used for text
shaping.

## Remarks

Possible direction values are:

- [`TTF_DIRECTION_LTR`](TTF_DIRECTION_LTR) (Left to Right)
- [`TTF_DIRECTION_RTL`](TTF_DIRECTION_RTL) (Right to Left)
- [`TTF_DIRECTION_TTB`](TTF_DIRECTION_TTB) (Top to Bottom)
- [`TTF_DIRECTION_BTT`](TTF_DIRECTION_BTT) (Bottom to Top)

If SDL_ttf was not built with HarfBuzz support, this function returns
[TTF_DIRECTION_LTR](TTF_DIRECTION_LTR).

## Thread Safety

This function should be called on the thread that created the font.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)
