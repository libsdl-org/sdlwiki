====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_GetFontWrappedAlign =

Query a font's current wrap alignment option.

== Syntax ==

<syntaxhighlight lang='c'>
int TTF_GetFontWrappedAlign(const TTF_Font *font);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to query.
|}

== Return Value ==

Returns the font's current wrap alignment option.

== Remarks ==

The wrap alignment option can be one of the following:

* <code>[[TTF_WRAPPED_ALIGN_LEFT]]</code>
* <code>[[TTF_WRAPPED_ALIGN_CENTER]]</code>
* <code>[[TTF_WRAPPED_ALIGN_RIGHT]]</code>

== Version ==

This function is available since SDL_ttf 2.20.0.

== Related Functions ==

:[[TTF_SetFontWrappedAlign]]

----
[[CategoryAPI]]


