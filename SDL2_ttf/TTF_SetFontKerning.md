###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_SetFontKerning

Set if kerning is allowed for a font.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
void TTF_SetFontKerning(TTF_Font *font, int allowed);

```

## Function Parameters

|                 |                                              |
| --------------- | -------------------------------------------- |
| **font**        | the font to set kerning on.                  |
| **allowed**     | non-zero to allow kerning, zero to disallow. |

## Remarks

Newly-opened fonts default to allowing kerning. This is generally a good
policy unless you have a strong reason to disable it, as it tends to
produce better rendering (with kerning disabled, some fonts might render
the word `kerning` as something that looks like `keming` for example).

## Version

This function is available since SDL_ttf 2.0.12.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

