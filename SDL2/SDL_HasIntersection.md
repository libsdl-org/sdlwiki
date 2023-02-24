====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HasIntersection =

Determine whether two rectangles intersect.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_HasIntersection(const SDL_Rect * A,
                             const SDL_Rect * B);
</syntaxhighlight>

== Function Parameters ==

{|
|'''A'''
|an [[SDL_Rect]] structure representing the first rectangle
|-
|'''B'''
|an [[SDL_Rect]] structure representing the second rectangle
|}

== Return Value ==

Returns [[SDL_TRUE]] if there is an intersection, [[SDL_FALSE]] otherwise.

== Remarks ==

If either pointer is NULL the function will return [[SDL_FALSE]].

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_IntersectRect]]

----
[[CategoryAPI]]


