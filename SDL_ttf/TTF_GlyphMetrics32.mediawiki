====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_GlyphMetrics32 =

Query the metrics (dimensions) of a font's 32-bit glyph.

== Syntax ==

<syntaxhighlight lang='c'>
int TTF_GlyphMetrics32(TTF_Font *font, Uint32 ch,
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

This is the same as [[TTF_GlyphMetrics]](), but takes a 32-bit character
instead of 16-bit, and thus can query a larger range. If you are sure
you'll have an SDL_ttf that's version 2.0.18 or newer, there's no reason
not to use this function exclusively.

== Version ==

This function is available since SDL_ttf 2.0.18.

----
[[CategoryAPI]]


