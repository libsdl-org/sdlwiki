====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetRectUnionFloat =

Calculate the union of two rectangles with float precision.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_GetRectUnionFloat(const SDL_FRect * A,
                    const SDL_FRect * B,
                    SDL_FRect * result);
</syntaxhighlight>

== Function Parameters ==

{|
|'''A'''
|an [[SDL_FRect]] structure representing the first rectangle
|-
|'''B'''
|an [[SDL_FRect]] structure representing the second rectangle
|-
|'''result'''
|an [[SDL_FRect]] structure filled in with the union of rectangles <code>A</code> and <code>B</code>
|}

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


