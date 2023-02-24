====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_OpenFont =

Create a font from a file, using a specified point size.

== Syntax ==

<syntaxhighlight lang='c'>
TTF_Font * TTF_OpenFont(const char *file, int ptsize);
</syntaxhighlight>

== Function Parameters ==

{|
|'''file'''
|path to font file.
|-
|'''ptsize'''
|point size to use for the newly-opened font.
|}

== Return Value ==

Returns a valid [[TTF_Font]], or NULL on error.

== Remarks ==

Some .fon fonts will have several sizes embedded in the file, so the point
size becomes the index of choosing which size. If the value is too high,
the last indexed size will be the default.

When done with the returned [[TTF_Font]], use [[TTF_CloseFont]]() to
dispose of it.

== Version ==

This function is available since SDL_ttf 2.0.12.

== Related Functions ==

:[[TTF_CloseFont]]

----
[[CategoryAPI]]


