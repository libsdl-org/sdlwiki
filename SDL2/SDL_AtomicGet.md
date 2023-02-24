====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_AtomicGet =

Get the value of an atomic variable.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_AtomicGet(SDL_atomic_t *a);
</syntaxhighlight>

== Function Parameters ==

{|
|'''a'''
|a pointer to an [[SDL_atomic_t]] variable
|}

== Return Value ==

Returns the current value of an atomic variable.

== Remarks ==

'''''Note: If you don't know what this function is for, you shouldn't use
it!'''''

== Version ==

This function is available since SDL 2.0.2.

== Related Functions ==

:[[SDL_AtomicSet]]

----
[[CategoryAPI]]


