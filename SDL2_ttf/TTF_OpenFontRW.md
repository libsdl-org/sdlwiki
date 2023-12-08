###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_OpenFontRW

Create a font from an SDL_RWops, using a specified point size.

## Syntax

```c
TTF_Font * TTF_OpenFontRW(SDL_RWops *src, int freesrc, int ptsize);

```

## Function Parameters

|                 |                                                                      |
| --------------- | -------------------------------------------------------------------- |
| **src**         | an SDL_RWops to provide a font file's data.                          |
| **freesrc**     | non-zero to close the RWops before returning, zero to leave it open. |
| **ptsize**      | point size to use for the newly-opened font.                         |

## Return Value

Returns a valid [TTF_Font](TTF_Font.md), or NULL on error.

## Remarks

Some .fon fonts will have several sizes embedded in the file, so the point
size becomes the index of choosing which size. If the value is too high,
the last indexed size will be the default.

If `freesrc` is non-zero, the RWops will be closed before returning,
whether this function succeeds or not. SDL_ttf reads everything it needs
from the RWops during this call in any case.

When done with the returned [TTF_Font](TTF_Font.md), use
[TTF_CloseFont](TTF_CloseFont.md)() to dispose of it.

## Version

This function is available since SDL_ttf 2.0.12.

## Related Functions

* [TTF_CloseFont](TTF_CloseFont.md)

----
[CategoryAPI](CategoryAPI.md)
