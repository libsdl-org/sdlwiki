====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_FreePalette =

Free a palette created with [[SDL_AllocPalette]]().

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_FreePalette(SDL_Palette * palette);
</syntaxhighlight>

== Function Parameters ==

{|
|'''palette'''
|the [[SDL_Palette]] structure to be freed
|}

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_AllocPalette]]

----
[[CategoryAPI]]


