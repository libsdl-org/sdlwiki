====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_ConvertSurface =

Copy an existing surface to a new surface of the specified format.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Surface* SDL_ConvertSurface
    (SDL_Surface * src, const SDL_PixelFormat * fmt, Uint32 flags);
</syntaxhighlight>

== Function Parameters ==

{|
|'''src'''
|the existing [[SDL_Surface]] structure to convert
|-
|'''fmt'''
|the [[SDL_PixelFormat]] structure that the new surface is optimized for
|-
|'''flags'''
|the flags are unused and should be set to 0; this is a leftover from SDL 1.2's API
|}

== Return Value ==

Returns the new [[SDL_Surface]] structure that is created or NULL if it
fails; call [[SDL_GetError]]() for more information.

== Remarks ==

This function is used to optimize images for faster ''repeat'' blitting.
This is accomplished by converting the original and storing the result as a
new surface. The new, optimized surface can then be used as the source for
future blits, making them faster.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_AllocFormat]]
:[[SDL_ConvertSurfaceFormat]]
:[[SDL_CreateRGBSurface]]

----
[[CategoryAPI]]


