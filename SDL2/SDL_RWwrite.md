====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RWwrite =

Write to an [[SDL_RWops]] data stream.

== Syntax ==

<syntaxhighlight lang='c'>
size_t SDL_RWwrite(SDL_RWops *context,
                   const void *ptr, size_t size,
                   size_t num);
</syntaxhighlight>

== Function Parameters ==

{|
|'''context'''
|a pointer to an [[SDL_RWops]] structure
|-
|'''ptr'''
|a pointer to a buffer containing data to write
|-
|'''size'''
|the size of an object to write, in bytes
|-
|'''num'''
|the number of objects to write
|}

== Return Value ==

Returns the number of objects written, which will be less than '''num''' on
error; call [[SDL_GetError]]() for more information.

== Remarks ==

This function writes exactly <code>num</code> objects each of size
<code>size</code> from the area pointed at by <code>ptr</code> to the
stream. If this fails for any reason, it'll return less than
<code>num</code> to demonstrate how far the write progressed. On success,
it returns <code>num</code>.

[[SDL_RWwrite]] is actually a function wrapper that calls the
[[SDL_RWops]]'s <code>write</code> method appropriately, to simplify
application development.

Prior to SDL 2.0.10, this function was a macro.

== Version ==

This function is available since SDL 2.0.10.

== Related Functions ==

:[[SDL_RWclose]]
:[[SDL_RWFromConstMem]]
:[[SDL_RWFromFile]]
:[[SDL_RWFromFP]]
:[[SDL_RWFromMem]]
:[[SDL_RWread]]
:[[SDL_RWseek]]

----
[[CategoryAPI]]


