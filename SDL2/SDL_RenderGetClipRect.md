====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderGetClipRect =

Get the clip rectangle for the current target.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_RenderGetClipRect(SDL_Renderer * renderer,
                           SDL_Rect * rect);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the rendering context from which clip rectangle should be queried
|-
|'''rect'''
|an [[SDL_Rect]] structure filled in with the current clipping area or an empty rectangle if clipping is disabled
|}

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_RenderIsClipEnabled]]
:[[SDL_RenderSetClipRect]]

----
[[CategoryAPI]]


