====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_SetSurfaceBlendMode =

Set the blend mode used for blit operations.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SetSurfaceBlendMode(SDL_Surface * surface,
                            SDL_BlendMode blendMode);
</syntaxhighlight>

== Function Parameters ==

{|
|'''surface'''
|the [[SDL_Surface]] structure to update
|-
|'''blendMode'''
|the [[SDL_BlendMode]] to use for blit blending
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

To copy a surface to another surface (or texture) without blending with the
existing data, the blendmode of the SOURCE surface should be set to
<code>[[SDL_BLENDMODE_NONE]]</code>.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetSurfaceBlendMode]]

----
[[CategoryAPI]]


