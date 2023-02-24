====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderFillRectsF =

Fill some number of rectangles on the current rendering target with the drawing color at subpixel precision.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_RenderFillRectsF(SDL_Renderer * renderer,
                         const SDL_FRect * rects,
                         int count);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|The renderer which should fill multiple rectangles.
|-
|'''rects'''
|A pointer to an array of destination rectangles.
|-
|'''count'''
|The number of rectangles.
|}

== Return Value ==

Return 0 on success, or -1 on error

== Version ==

This function is available since SDL 2.0.10.

----
[[CategoryAPI]]


