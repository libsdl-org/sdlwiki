====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_CloseFont =

Dispose of a previously-created font.

== Syntax ==

<syntaxhighlight lang='c'>
void TTF_CloseFont(TTF_Font *font);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to dispose of.
|}

== Remarks ==

Call this when done with a font. This function will free any resources
associated with it. It is safe to call this function on NULL, for example
on the result of a failed call to [[TTF_OpenFont]]().

The font is not valid after being passed to this function. String pointers
from functions that return information on this font, such as
[[TTF_FontFaceFamilyName]]() and [[TTF_FontFaceStyleName]](), are no longer
valid after this call, as well.

== Version ==

This function is available since SDL_ttf 2.0.12.

== Related Functions ==

:[[TTF_OpenFont]]
:[[TTF_OpenFontIndexDPIRW]]
:[[TTF_OpenFontRW]]
:[[TTF_OpenFontDPI]]
:[[TTF_OpenFontDPIRW]]
:[[TTF_OpenFontIndex]]
:[[TTF_OpenFontIndexDPI]]
:[[TTF_OpenFontIndexDPIRW]]
:[[TTF_OpenFontIndexRW]]

----
[[CategoryAPI]]


