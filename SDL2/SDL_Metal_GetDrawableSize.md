====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_Metal_GetDrawableSize =

Get the size of a window's underlying drawable in pixels (for use with setting viewport, scissor & etc).

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_Metal_GetDrawableSize(SDL_Window* window, int *w,
                               int *h);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|[[SDL_Window]] from which the drawable size should be queried
|-
|'''w'''
|Pointer to variable for storing the width in pixels, may be NULL
|-
|'''h'''
|Pointer to variable for storing the height in pixels, may be NULL
|}

== Version ==

This function is available since SDL 2.0.14.

== Related Functions ==

:[[SDL_GetWindowSize]]
:[[SDL_CreateWindow]]

----
[[CategoryAPI]]


