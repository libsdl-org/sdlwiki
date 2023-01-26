====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_DestroyRW =

Use this function to free an [[SDL_RWops]] structure allocated by [[SDL_CreateRW]]().

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_DestroyRW(SDL_RWops * area);
</syntaxhighlight>

== Function Parameters ==

{|
|'''area'''
|the [[SDL_RWops]] structure to be freed
|}

== Remarks ==

Applications do not need to use this function unless they are providing
their own [[SDL_RWops]] implementation. If you just need a [[SDL_RWops]] to
read/write a common data source, you should use the built-in
implementations in SDL, like [[SDL_RWFromFile]]() or [[SDL_RWFromMem]](),
etc, and call the '''close''' method on those [[SDL_RWops]] pointers when
you are done with them.

Only use [[SDL_DestroyRW]]() on pointers returned by [[SDL_CreateRW]]().
The pointer is invalid as soon as this function returns. Any extra memory
allocated during creation of the [[SDL_RWops]] is not freed by
[[SDL_DestroyRW]](); the programmer must be responsible for managing that
memory in their '''close''' method.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_CreateRW]]

----
[[CategoryAPI]]


