====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_SetFontWrappedAlign =

Set a font's current wrap alignment option.

== Syntax ==

<syntaxhighlight lang='c'>
void TTF_SetFontWrappedAlign(TTF_Font *font, int align);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to set a new wrap alignment option on.
|-
|'''align'''
|the new wrap alignment option.
|}

== Remarks ==

The wrap alignment option can be one of the following:

* <code>[[TTF_WRAPPED_ALIGN_LEFT]]</code>
* <code>[[TTF_WRAPPED_ALIGN_CENTER]]</code>
* <code>[[TTF_WRAPPED_ALIGN_RIGHT]]</code>

== Version ==

This function is available since SDL_ttf 2.20.0.

== Related Functions ==

:[[TTF_GetFontWrappedAlign]]

----
[[CategoryAPI]]


