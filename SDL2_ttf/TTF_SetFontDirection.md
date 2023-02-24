###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontDirection

Set direction to be used for text shaping by a font.

## Syntax

```c
int TTF_SetFontDirection(TTF_Font *font, TTF_Direction direction);

```

## Function Parameters

|                   |                                      |
| ----------------- | ------------------------------------ |
| **font**          | the font to specify a direction for. |
| **direction**     | the new direction for text to flow.  |

## Return Value

Returns 0 on success, or -1 on error.

## Remarks

Any value supplied here will override the global direction set with the
deprecated [TTF_SetDirection](TTF_SetDirection)().

Possible direction values are:

- [`TTF_DIRECTION_LTR`](TTF_DIRECTION_LTR) (Left to Right)
- [`TTF_DIRECTION_RTL`](TTF_DIRECTION_RTL) (Right to Left)
- [`TTF_DIRECTION_TTB`](TTF_DIRECTION_TTB) (Top to Bottom)
- [`TTF_DIRECTION_BTT`](TTF_DIRECTION_BTT) (Bottom to Top)

If SDL_ttf was not built with HarfBuzz support, this function returns -1.

## Version

This function is available since SDL_ttf 2.20.0.

----
[CategoryAPI](CategoryAPI)

