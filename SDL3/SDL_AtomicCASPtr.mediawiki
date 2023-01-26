====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_AtomicCASPtr =

Set a pointer to a new value if it is currently an old value.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_AtomicCASPtr(void **a, void *oldval, void *newval);
</syntaxhighlight>

== Function Parameters ==

{|
|'''a'''
|a pointer to a pointer
|-
|'''oldval'''
|the old pointer value
|-
|'''newval'''
|the new pointer value
|}

== Return Value ==

Returns [[SDL_TRUE]] if the pointer was set, [[SDL_FALSE]] otherwise.

== Remarks ==

'''''Note: If you don't know what this function is for, you shouldn't use
it!'''''

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_AtomicCAS]]
:[[SDL_AtomicGetPtr]]
:[[SDL_AtomicSetPtr]]

----
[[CategoryAPI]], [[CategoryAtomic]]


