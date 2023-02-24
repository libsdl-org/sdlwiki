====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_SizeText =

Calculate the dimensions of a rendered string of Latin1 text.

== Syntax ==

<syntaxhighlight lang='c'>
int TTF_SizeText(TTF_Font *font, const char *text, int *w, int *h);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to query.
|-
|'''text'''
|text to calculate, in Latin1 encoding.
|-
|'''w'''
|will be filled with width, in pixels, on return.
|-
|'''h'''
|will be filled with height, in pixels, on return.
|}

== Return Value ==

Returns 0 if successful, -1 on error.

== Remarks ==

This will report the width and height, in pixels, of the space that the
specified string will take to fully render.

This does not need to render the string to do this calculation.

You almost certainly want [[TTF_SizeUTF8]]() unless you're sure you have a
1-byte Latin1 encoding. US ASCII characters will work with either function,
but most other Unicode characters packed into a <code>const char *</code>
will need UTF-8.

== Version ==

This function is available since SDL_ttf 2.0.12.

== Related Functions ==

:[[TTF_SizeUTF8]]
:[[TTF_SizeUNICODE]]

----
[[CategoryAPI]]


