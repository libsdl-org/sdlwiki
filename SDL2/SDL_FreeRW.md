====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_FreeRW =

Use this function to free an [[SDL_RWops]] structure allocated by [[SDL_AllocRW]]().

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_FreeRW(SDL_RWops * area);
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

Only use [[SDL_FreeRW]]() on pointers returned by [[SDL_AllocRW]](). The
pointer is invalid as soon as this function returns. Any extra memory
allocated during creation of the [[SDL_RWops]] is not freed by
[[SDL_FreeRW]](); the programmer must be responsible for managing that
memory in their '''close''' method.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_AllocRW]]

----
[[CategoryAPI]]


