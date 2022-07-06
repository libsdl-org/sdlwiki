====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_GetFontStyle =

Query a font's current style.

== Syntax ==

<syntaxhighlight lang='c'>
int TTF_GetFontStyle(const TTF_Font *font);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to query.
|}

== Return Value ==

Returns the current font style, as a set of bit flags.

== Remarks ==

The font styles are a set of bit flags, OR'd together:

* <code>[[TTF_STYLE_NORMAL]]</code> (is zero)
* <code>[[TTF_STYLE_BOLD]]</code>
* <code>[[TTF_STYLE_ITALIC]]</code>
* <code>[[TTF_STYLE_UNDERLINE]]</code>
* <code>[[TTF_STYLE_STRIKETHROUGH]]</code>

== Version ==

This function is available since SDL_ttf 2.0.12.

== Related Functions ==

:[[TTF_SetFontStyle]]

----
[[CategoryAPI]]


