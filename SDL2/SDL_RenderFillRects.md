====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderFillRects =

Fill some number of rectangles on the current rendering target with the drawing color.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_RenderFillRects(SDL_Renderer * renderer,
                        const SDL_Rect * rects,
                        int count);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the rendering context
|-
|'''rects'''
|an array of [[SDL_Rect]] structures representing the rectangles to be filled
|-
|'''count'''
|the number of rectangles
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_RenderDrawLine]]
:[[SDL_RenderDrawLines]]
:[[SDL_RenderDrawPoint]]
:[[SDL_RenderDrawPoints]]
:[[SDL_RenderDrawRect]]
:[[SDL_RenderDrawRects]]
:[[SDL_RenderFillRect]]
:[[SDL_RenderPresent]]

----
[[CategoryAPI]]


