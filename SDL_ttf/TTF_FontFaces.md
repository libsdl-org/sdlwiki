====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_FontFaces =

Query the number of faces of a font.

== Syntax ==

<syntaxhighlight lang='c'>
long TTF_FontFaces(const TTF_Font *font);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to query.
|}

== Return Value ==

Returns the number of FreeType font faces.

== Version ==

This function is available since SDL_ttf 2.0.12.

----
[[CategoryAPI]]


