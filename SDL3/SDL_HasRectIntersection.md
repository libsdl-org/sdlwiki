====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_HasRectIntersection =

Determine whether two rectangles intersect.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_HasRectIntersection(const SDL_Rect * A,
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

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetRectIntersection]]

----
[[CategoryAPI]]


