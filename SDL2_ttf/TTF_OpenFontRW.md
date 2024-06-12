###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_OpenFontRW

Create a font from an SDL_RWops, using a specified point size.

## Header File

Defined in [<SDL_ttf.h>](https://github.com/libsdl-org/SDL_ttf/blob/SDL2/include/SDL_ttf.h)

## Syntax

```c
TTF_Font * TTF_OpenFontRW(SDL_RWops *src, int freesrc, int ptsize);
```

## Function Parameters

|             |             |                                                                             |
| ----------- | ----------- | --------------------------------------------------------------------------- |
| SDL_RWops * | **src**     | an SDL_RWops to provide a font file's data.                                 |
| int         | **freesrc** | non-zero to close the RWops when the font is closed, zero to leave it open. |
| int         | **ptsize**  | point size to use for the newly-opened font.                                |

## Return Value

([TTF_Font](TTF_Font) *) Returns a valid [TTF_Font](TTF_Font), or NULL on
error.

## Remarks

Some .fon fonts will have several sizes embedded in the file, so the point
size becomes the index of choosing which size. If the value is too high,
the last indexed size will be the default.

If `freesrc` is non-zero, the RWops will be automatically closed once the
font is closed. Otherwise you should close the RWops yourself after closing
the font.

When done with the returned [TTF_Font](TTF_Font), use
[TTF_CloseFont](TTF_CloseFont)() to dispose of it.

## Version

This function is available since SDL_ttf 2.0.12.

## See Also

- [TTF_CloseFont](TTF_CloseFont)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

