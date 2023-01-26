====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderGetIntegerScale =

Get whether integer scales are forced for resolution-independent rendering.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_RenderGetIntegerScale(SDL_Renderer * renderer);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the renderer from which integer scaling should be queried
|}

== Return Value ==

Returns [[SDL_TRUE]] if integer scales are forced or [[SDL_FALSE]] if not
and on failure; call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.5.

== Related Functions ==

:[[SDL_RenderSetIntegerScale]]

----
[[CategoryAPI]]


