====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_FreeWAV =

Free data previously allocated with [[SDL_LoadWAV]]() or [[SDL_LoadWAV_RW]]().

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_FreeWAV(Uint8 * audio_buf);
</syntaxhighlight>

== Function Parameters ==

{|
|'''audio_buf'''
|a pointer to the buffer created by [[SDL_LoadWAV]]() or [[SDL_LoadWAV_RW]]()
|}

== Remarks ==

After a WAVE file has been opened with [[SDL_LoadWAV]]() or
[[SDL_LoadWAV_RW]]() its data can eventually be freed with
[[SDL_FreeWAV]](). It is safe to call this function with a NULL pointer.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_LoadWAV]]
:[[SDL_LoadWAV_RW]]

----
[[CategoryAPI]]


