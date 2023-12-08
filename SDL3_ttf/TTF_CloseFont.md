###### (This function is part of SDL_ttf, a separate library from SDL.)
# TTF_CloseFont

Dispose of a previously-created font.

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
on the result of a failed call to [TTF_OpenFont](TTF_OpenFont.md)().

The font is not valid after being passed to this function. String pointers
from functions that return information on this font, such as
[TTF_FontFaceFamilyName](TTF_FontFaceFamilyName.md)() and
[TTF_FontFaceStyleName](TTF_FontFaceStyleName.md)(), are no longer valid after
this call, as well.

## Version

This function is available since SDL_ttf 3.0.0.

## Related Functions

* [TTF_OpenFont](TTF_OpenFont.md)
* [TTF_OpenFontIndexDPIRW](TTF_OpenFontIndexDPIRW.md)
* [TTF_OpenFontRW](TTF_OpenFontRW.md)
* [TTF_OpenFontDPI](TTF_OpenFontDPI.md)
* [TTF_OpenFontDPIRW](TTF_OpenFontDPIRW.md)
* [TTF_OpenFontIndex](TTF_OpenFontIndex.md)
* [TTF_OpenFontIndexDPI](TTF_OpenFontIndexDPI.md)
* [TTF_OpenFontIndexDPIRW](TTF_OpenFontIndexDPIRW.md)
* [TTF_OpenFontIndexRW](TTF_OpenFontIndexRW.md)

----
[CategoryAPI](CategoryAPI.md)
