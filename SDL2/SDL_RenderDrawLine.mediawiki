====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderDrawLine =

Draw a line on the current rendering target.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_RenderDrawLine(SDL_Renderer * renderer,
                       int x1, int y1, int x2, int y2);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the rendering context
|-
|'''x1'''
|the x coordinate of the start point
|-
|'''y1'''
|the y coordinate of the start point
|-
|'''x2'''
|the x coordinate of the end point
|-
|'''y2'''
|the y coordinate of the end point
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

[[SDL_RenderDrawLine]]() draws the line to include both end points. If you
want to draw multiple, connecting lines use [[SDL_RenderDrawLines]]()
instead.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_RenderDrawLines]]
:[[SDL_RenderDrawPoint]]
:[[SDL_RenderDrawPoints]]
:[[SDL_RenderDrawRect]]
:[[SDL_RenderDrawRects]]
:[[SDL_RenderFillRect]]
:[[SDL_RenderFillRects]]
:[[SDL_RenderPresent]]
:[[SDL_SetRenderDrawBlendMode]]
:[[SDL_SetRenderDrawColor]]

----
[[CategoryAPI]]


