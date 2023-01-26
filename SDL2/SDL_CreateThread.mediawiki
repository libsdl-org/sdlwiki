====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_CreateThread =

Create a new thread with a default stack size.

== Syntax ==

<syntaxhighlight lang='c'>
extern DECLSPEC SDL_Thread *SDLCALL
SDL_CreateThread(SDL_ThreadFunction fn, const char *name, void *data);
</syntaxhighlight>

== Function Parameters ==

{|
|'''fn'''
|the [[SDL_ThreadFunction]] function to call in the new thread
|-
|'''name'''
|the name of the thread
|-
|'''data'''
|a pointer that is passed to <code>fn</code>
|}

== Return Value ==

Returns an opaque pointer to the new thread object on success, NULL if the
new thread could not be created; call [[SDL_GetError]]() for more
information.

== Remarks ==

This is equivalent to calling:

<syntaxhighlight lang='c'>
SDL_CreateThreadWithStackSize(fn, name, 0, data);
</syntaxhighlight>

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateThreadWithStackSize]]
:[[SDL_WaitThread]]

----
[[CategoryAPI]]


