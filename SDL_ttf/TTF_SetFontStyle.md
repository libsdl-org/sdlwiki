====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_SetFontStyle =

Set a font's current style.

== Syntax ==

<syntaxhighlight lang='c'>
void TTF_SetFontStyle(TTF_Font *font, int style);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to set a new style on.
|-
|'''style'''
|the new style values to set, OR'd together.
|}

== Remarks ==

Setting the style clears already-generated glyphs, if any, from the cache.

The font styles are a set of bit flags, OR'd together:

* <code>[[TTF_STYLE_NORMAL]]</code> (is zero)
* <code>[[TTF_STYLE_BOLD]]</code>
* <code>[[TTF_STYLE_ITALIC]]</code>
* <code>[[TTF_STYLE_UNDERLINE]]</code>
* <code>[[TTF_STYLE_STRIKETHROUGH]]</code>

== Version ==

This function is available since SDL_ttf 2.0.12.

== Related Functions ==

:[[TTF_GetFontStyle]]

----
[[CategoryAPI]]


