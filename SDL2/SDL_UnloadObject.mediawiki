====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_UnloadObject =

Unload a shared object from memory.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_UnloadObject(void *handle);
</syntaxhighlight>

== Function Parameters ==

{|
|'''handle'''
|a valid shared object handle returned by [[SDL_LoadObject]]()
|}

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_LoadFunction]]
:[[SDL_LoadObject]]

----
[[CategoryAPI]]


