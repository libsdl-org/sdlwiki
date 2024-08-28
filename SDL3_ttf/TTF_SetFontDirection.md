###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontDirection

Set direction to be used for text shaping by a font.

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
SDL_bool TTF_SetFontDirection(TTF_Font *font, TTF_Direction direction);
```

## Function Parameters

|                                |               |                                      |
| ------------------------------ | ------------- | ------------------------------------ |
| [TTF_Font](TTF_Font) *         | **font**      | the font to specify a direction for. |
| [TTF_Direction](TTF_Direction) | **direction** | the new direction for text to flow.  |

## Return Value

(SDL_bool) Returns SDL_TRUE on success or SDL_FALSE on failure; call
SDL_GetError() for more information.

## Remarks

Possible direction values are:

- [`TTF_DIRECTION_LTR`](TTF_DIRECTION_LTR) (Left to Right)
- [`TTF_DIRECTION_RTL`](TTF_DIRECTION_RTL) (Right to Left)
- [`TTF_DIRECTION_TTB`](TTF_DIRECTION_TTB) (Top to Bottom)
- [`TTF_DIRECTION_BTT`](TTF_DIRECTION_BTT) (Bottom to Top)

If SDL_ttf was not built with HarfBuzz support, this function returns -1.

## Version

This function is available since SDL_ttf 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

