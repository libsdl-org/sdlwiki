====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HasSurfaceRLE =

Returns whether the surface is RLE enabled 

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_HasSurfaceRLE(SDL_Surface * surface);
</syntaxhighlight>

== Function Parameters ==

{|
|'''surface'''
|the [[SDL_Surface]] structure to query
|}

== Return Value ==

Returns [[SDL_TRUE]] if the surface is RLE enabled, [[SDL_FALSE]]
otherwise.

== Remarks ==

It is safe to pass a NULL <code>surface</code> here; it will return
[[SDL_FALSE]].

== Version ==

This function is available since SDL 2.0.14.

== Related Functions ==

:[[SDL_SetSurfaceRLE]]

----
[[CategoryAPI]]


