====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_UnlockSurface =

Release a surface after directly accessing the pixels.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_UnlockSurface(SDL_Surface *surface);
</syntaxhighlight>

== Function Parameters ==

{|
|'''surface'''
|the [[SDL_Surface]] structure to be unlocked
|}

== Version ==

This function is available since SDL 3.0.0.

== Code Examples ==

<<Include(SDL_LockSurface, , , from="== Code Examples ==", to="== Remarks ==")>>

== Related Functions ==

:[[SDL_LockSurface]]

----
[[CategoryAPI]], [[CategorySurface]]


