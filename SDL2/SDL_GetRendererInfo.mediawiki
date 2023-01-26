====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetRendererInfo =

Get information about a rendering context.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GetRendererInfo(SDL_Renderer * renderer,
                        SDL_RendererInfo * info);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the rendering context
|-
|'''info'''
|an [[SDL_RendererInfo]] structure filled with information about the current renderer
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateRenderer]]

----
[[CategoryAPI]]


