###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetDirection

Set a global direction to be used for text shaping.

## Deprecated

This function expects an hb_direction_t value, from HarfBuzz, cast to an
int, and affects all fonts globally. Please use
[TTF_SetFontDirection](TTF_SetFontDirection.md)() instead, which uses an enum
supplied by SDL_ttf itself and operates on a per-font basis.

This is a global setting; fonts will favor a value set with
[TTF_SetFontDirection](TTF_SetFontDirection.md)(), but if they have not had
one explicitly set, they will use the value specified here.

The default value is `HB_DIRECTION_LTR` (left-to-right text flow).

## Syntax

```c
int TTF_SetDirection(int direction); /* hb_direction_t */

```

## Function Parameters

|                   |                          |
| ----------------- | ------------------------ |
| **direction**     | an hb_direction_t value. |

## Return Value

Returns 0, or -1 if SDL_ttf is not compiled with HarfBuzz support.

## Version

This function is available since SDL_ttf 2.0.18.

## Related Functions

* [TTF_SetFontDirection](TTF_SetFontDirection.md)

----
[CategoryAPI](CategoryAPI.md)
