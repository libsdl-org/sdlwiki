====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_LoadBMP_RW =

Load a BMP image from a seekable SDL data stream.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Surface* SDL_LoadBMP_RW(SDL_RWops * src,
                            int freesrc);
</syntaxhighlight>

== Function Parameters ==

{|
|'''src'''
|the data stream for the surface
|-
|'''freesrc'''
|non-zero to close the stream after being read
|}

== Return Value ==

Returns a pointer to a new [[SDL_Surface]] structure or NULL if there was
an error; call [[SDL_GetError]]() for more information.

== Remarks ==

The new surface should be freed with [[SDL_FreeSurface]](). Not doing so
will result in a memory leak.

src is an open [[SDL_RWops]] buffer, typically loaded with
[[SDL_RWFromFile]]. Alternitavely, you might also use the macro
[[SDL_LoadBMP]] to load a bitmap from a file, convert it to an
[[SDL_Surface]] and then close the file.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_FreeSurface]]
:[[SDL_RWFromFile]]
:[[SDL_LoadBMP]]
:[[SDL_SaveBMP_RW]]

----
[[CategoryAPI]]


