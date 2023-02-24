====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_RenderUNICODE_LCD =

Render UCS-2 text at LCD subpixel quality to a new ARGB surface.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Surface * TTF_RenderUNICODE_LCD(TTF_Font *font,
                const Uint16 *text, SDL_Color fg, SDL_Color bg);
</syntaxhighlight>

== Function Parameters ==

{|
|'''font'''
|the font to render with.
|-
|'''text'''
|text to render, in UCS-2 encoding.
|-
|'''fg'''
|the foreground color for the text.
|-
|'''bg'''
|the background color for the text.
|}

== Return Value ==

Returns a new 32-bit, ARGB surface, or NULL if there was an error.

== Remarks ==

This function will allocate a new 32-bit, ARGB surface, and render
alpha-blended text using FreeType's LCD subpixel rendering. This function
returns the new surface, or NULL if there was an error.

This will not word-wrap the string; you'll get a surface with a single line
of text, as long as the string requires. You can use
[[TTF_RenderUNICODE_LCD_Wrapped]]() instead if you need to wrap the output
to multiple lines.

This will not wrap on newline characters.

Please note that this function is named "Unicode" but currently expects
UCS-2 encoding (16 bits per codepoint). This does not give you access to
large Unicode values, such as emoji glyphs. These codepoints are accessible
through the UTF-8 version of this function.

You can render at other quality levels with [[TTF_RenderUNICODE_Solid]],
[[TTF_RenderUNICODE_Shaded]], and [[TTF_RenderUNICODE_Blended]].

== Version ==

This function is available since SDL_ttf 2.20.0.

== Related Functions ==

:[[TTF_RenderUTF8_LCD]]

----
[[CategoryAPI]]


