====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetWindowPixelFormat =

Get the pixel format associated with the window.

== Syntax ==

<syntaxhighlight lang='c'>
Uint32 SDL_GetWindowPixelFormat(SDL_Window * window);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to query
|}

== Return Value ==

Returns the pixel format of the window on success or
[[SDL_PIXELFORMAT_UNKNOWN]] on failure; call [[SDL_GetError]]() for more
information.

== Version ==

This function is available since SDL 2.0.0.

----
[[CategoryAPI]]


