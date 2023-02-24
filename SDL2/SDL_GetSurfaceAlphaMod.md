====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetSurfaceAlphaMod =

Get the additional alpha value used in blit operations.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GetSurfaceAlphaMod(SDL_Surface * surface,
                           Uint8 * alpha);
</syntaxhighlight>

== Function Parameters ==

{|
|'''surface'''
|the [[SDL_Surface]] structure to query
|-
|'''alpha'''
|a pointer filled in with the current alpha value
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetSurfaceColorMod]]
:[[SDL_SetSurfaceAlphaMod]]

----
[[CategoryAPI]]


