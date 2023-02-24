====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HapticIndex =

Get the index of a haptic device.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_HapticIndex(SDL_Haptic * haptic);
</syntaxhighlight>

== Function Parameters ==

{|
|'''haptic'''
|the [[SDL_Haptic]] device to query
|}

== Return Value ==

Returns the index of the specified haptic device or a negative error code
on failure; call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_HapticOpen]]
:[[SDL_HapticOpened]]

----
[[CategoryAPI]]


