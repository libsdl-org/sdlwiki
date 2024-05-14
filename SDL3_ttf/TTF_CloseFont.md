###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_CloseFont

Dispose of a previously-created font.

## Header File

Defined in SDL_ttf.h

## Syntax

```c
void TTF_CloseFont(TTF_Font *font);

```

## Function Parameters

|              |                         |
| ------------ | ----------------------- |
| **font**     | the font to dispose of. |

## Remarks

Call this when done with a font. This function will free any resources
associated with it. It is safe to call this function on NULL, for example
on the result of a failed call to [TTF_OpenFont](TTF_OpenFont)().

The font is not valid after being passed to this function. String pointers
from functions that return information on this font, such as
[TTF_FontFaceFamilyName](TTF_FontFaceFamilyName)() and
[TTF_FontFaceStyleName](TTF_FontFaceStyleName)(), are no longer valid after
this call, as well.

## Version

This function is available since SDL_ttf 3.0.0.

## See Also

- [TTF_OpenFont](TTF_OpenFont)
- [TTF_OpenFontIndexDPIIO](TTF_OpenFontIndexDPIIO)
- [TTF_OpenFontIO](TTF_OpenFontIO)
- [TTF_OpenFontDPI](TTF_OpenFontDPI)
- [TTF_OpenFontDPIIO](TTF_OpenFontDPIIO)
- [TTF_OpenFontIndex](TTF_OpenFontIndex)
- [TTF_OpenFontIndexDPI](TTF_OpenFontIndexDPI)
- [TTF_OpenFontIndexDPIIO](TTF_OpenFontIndexDPIIO)
- [TTF_OpenFontIndexIO](TTF_OpenFontIndexIO)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

