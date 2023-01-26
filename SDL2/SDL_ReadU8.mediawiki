====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_ReadU8 =

Use this function to read a byte from an [[SDL_RWops]].

== Syntax ==

<syntaxhighlight lang='c'>
Uint8 SDL_ReadU8(SDL_RWops * src);
</syntaxhighlight>

== Function Parameters ==

{|
|'''src'''
|the [[SDL_RWops]] to read from
|}

== Return Value ==

Returns the read byte on success or 0 on failure; call [[SDL_GetError]]()
for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_WriteU8]]

----
[[CategoryAPI]]


