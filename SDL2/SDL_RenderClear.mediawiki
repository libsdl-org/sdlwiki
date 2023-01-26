====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderClear =

Clear the current rendering target with the drawing color.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_RenderClear(SDL_Renderer * renderer);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the rendering context
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

This function clears the entire rendering target, ignoring the viewport and
the clip rectangle.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_SetRenderDrawColor]]

----
[[CategoryAPI]]


