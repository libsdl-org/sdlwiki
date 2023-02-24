====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_TLSSet =

Set the current thread's value associated with a thread local storage ID.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_TLSSet(SDL_TLSID id, const void *value, void (SDLCALL *destructor)(void*));
</syntaxhighlight>

== Function Parameters ==

{|
|'''id'''
|the thread local storage ID
|-
|'''value'''
|the value to associate with the ID for the current thread
|-
|'''destructor'''
|a function called when the thread exits, to free the value
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

The function prototype for <code>destructor</code> is:

<syntaxhighlight lang='c'>
void destructor(void *value)
</syntaxhighlight>

where its parameter <code>value</code> is what was passed as
<code>value</code> to [[SDL_TLSSet]]().

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_TLSCreate]]
:[[SDL_TLSGet]]

----
[[CategoryAPI]]


