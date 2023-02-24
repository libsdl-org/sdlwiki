====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_GlyphMetrics =

Query the metrics (dimensions) of a font's 16-bit glyph.

== Syntax ==

<syntaxhighlight lang='c'>
int TTF_GlyphMetrics(TTF_Font *font, Uint16 ch,
int *minx, int *maxx,
int *miny, int *maxy, int *advance);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to query.
|-
|'''ch'''
|the character code to check.
|}

== Remarks ==

To understand what these metrics mean, here is a useful link:

https://freetype.sourceforge.net/freetype2/docs/tutorial/step2.html

Note that this version of the function takes a 16-bit character code, which
covers the Basic Multilingual Plane, but is insufficient to cover the
entire set of possible Unicode values, including emoji glyphs. You should
use [[TTF_GlyphMetrics32]]() instead, which offers the same functionality
but takes a 32-bit codepoint instead.

The only reason to use this function is that it was available since the
beginning of time, more or less.

== Version ==

This function is available since SDL_ttf 2.0.12.

== Related Functions ==

:[[TTF_GlyphMetrics32]]

----
[[CategoryAPI]]


