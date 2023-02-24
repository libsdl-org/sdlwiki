====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderGetScale =

Get the drawing scale for the current target.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_RenderGetScale(SDL_Renderer * renderer,
                       float *scaleX, float *scaleY);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the renderer from which drawing scale should be queried
|-
|'''scaleX'''
|a pointer filled in with the horizontal scaling factor
|-
|'''scaleY'''
|a pointer filled in with the vertical scaling factor
|}

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_RenderSetScale]]

----
[[CategoryAPI]]


