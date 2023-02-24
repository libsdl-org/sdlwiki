====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
= SDL_TLSGet =

Get the current thread's value associated with a thread local storage ID.

== Syntax ==

<syntaxhighlight lang='c'>
void * SDL_TLSGet(SDL_TLSID id);
</syntaxhighlight>

== Function Parameters ==

{|
|'''id'''
|the thread local storage ID
|}

== Return Value ==

Returns the value associated with the ID for the current thread or NULL if
no value has been set; call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_TLSCreate]]
:[[SDL_TLSSet]]

----
[[CategoryAPI]], [[CategoryThread]], [[CategoryDraft]]
<!-- #See the Style Guide for instructions on editing the footer. -->


