====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_FontDescent =

Query the offset from the baseline to the bottom of a font.

== Syntax ==

<syntaxhighlight lang='c'>
int TTF_FontDescent(const TTF_Font *font);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to query.
|}

== Return Value ==

Returns the font's descent.

== Remarks ==

This is a negative value, relative to the baseline.

== Version ==

This function is available since SDL_ttf 2.0.12.

----
[[CategoryAPI]]


