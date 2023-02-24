====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_SetRenderDrawBlendMode =

Set the blend mode used for drawing operations (Fill and Line).

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SetRenderDrawBlendMode(SDL_Renderer * renderer,
                               SDL_BlendMode blendMode);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the rendering context
|-
|'''blendMode'''
|the [[SDL_BlendMode]] to use for blending
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

If the blend mode is not supported, the closest supported mode is chosen.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetRenderDrawBlendMode]]
:[[SDL_RenderDrawLine]]
:[[SDL_RenderDrawLines]]
:[[SDL_RenderDrawPoint]]
:[[SDL_RenderDrawPoints]]
:[[SDL_RenderDrawRect]]
:[[SDL_RenderDrawRects]]
:[[SDL_RenderFillRect]]
:[[SDL_RenderFillRects]]

----
[[CategoryAPI]]


