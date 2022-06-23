====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_MeasureText =

Calculate how much of a Latin1 string will fit in a given width.

== Syntax ==

<syntaxhighlight lang='c'>
int TTF_MeasureText(TTF_Font *font, const char *text, int measure_width, int *extent, int *count);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to query.
|-
|'''text'''
|text to calculate, in Latin1 encoding.
|-
|'''measure_width'''
|maximum width, in pixels, available for the string.
|-
|'''count'''
|on return, filled with number of characters that can be rendered.
|-
|'''extent'''
|on return, filled with latest calculated width.
|}

== Return Value ==

Returns 0 if successful, -1 on error.

== Remarks ==

This reports the number of characters that can be rendered before reaching
<code>measure_width</code>.

This does not need to render the string to do this calculation.

You almost certainly want [[TTF_MeasureUTF8]]() unless you're sure you have
a 1-byte Latin1 encoding. US ASCII characters will work with either
function, but most other Unicode characters packed into a <code>const char
*</code> will need UTF-8.

== Version ==

This function is available since SDL_ttf 2.0.18.

== Related Functions ==

:[[TTF_MeasureText]]
:[[TTF_MeasureUTF8]]
:[[TTF_MeasureUNICODE]]

----
[[CategoryAPI]]


