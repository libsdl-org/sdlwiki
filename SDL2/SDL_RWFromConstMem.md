====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RWFromConstMem =

Use this function to prepare a read-only memory buffer for use with RWops.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_RWops* SDL_RWFromConstMem(const void *mem,
                              int size);
</syntaxhighlight>

== Function Parameters ==

{|
|'''mem'''
|a pointer to a read-only buffer to feed an [[SDL_RWops]] stream
|-
|'''size'''
|the buffer size, in bytes
|}

== Return Value ==

Returns a pointer to a new [[SDL_RWops]] structure, or NULL if it fails;
call [[SDL_GetError]]() for more information.

== Remarks ==

This function sets up an [[SDL_RWops]] struct based on a memory area of a
certain size. It assumes the memory area is not writable.

Attempting to write to this RWops stream will report an error without
writing to the memory buffer.

This memory buffer is not copied by the RWops; the pointer you provide must
remain valid until you close the stream. Closing the stream will not free
the original buffer.

If you need to write to a memory buffer, you should use [[SDL_RWFromMem]]()
with a writable buffer of memory instead.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_RWclose]]
:[[SDL_RWFromConstMem]]
:[[SDL_RWFromFile]]
:[[SDL_RWFromFP]]
:[[SDL_RWFromMem]]
:[[SDL_RWread]]
:[[SDL_RWseek]]
:[[SDL_RWtell]]

----
[[CategoryAPI]]


