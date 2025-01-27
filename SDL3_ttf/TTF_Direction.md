###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_Direction

Direction flags

## Header File

Defined in [<SDL3_ttf/SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/main/include/SDL3_ttf/SDL_ttf.h)

## Syntax

```c
typedef enum TTF_Direction
{
  TTF_DIRECTION_INVALID = 0,
  TTF_DIRECTION_LTR = 4,        /**< Left to Right */
  TTF_DIRECTION_RTL,            /**< Right to Left */
  TTF_DIRECTION_TTB,            /**< Top to Bottom */
  TTF_DIRECTION_BTT             /**< Bottom to Top */
} TTF_Direction;
```

## Remarks

The values here are chosen to match hb_direction_t.

## Version

This enum is available since SDL_ttf 3.0.0.

## See Also

- [TTF_SetFontDirection](TTF_SetFontDirection)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategorySDLTTF](CategorySDLTTF)

