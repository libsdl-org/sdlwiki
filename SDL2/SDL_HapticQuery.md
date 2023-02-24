====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HapticQuery =

Get the haptic device's supported features in bitwise manner.

== Syntax ==

<syntaxhighlight lang='c'>
unsigned int SDL_HapticQuery(SDL_Haptic * haptic);
</syntaxhighlight>

== Function Parameters ==

{|
|'''haptic'''
|the [[SDL_Haptic]] device to query
|}

== Return Value ==

Returns a list of supported haptic features in bitwise manner (OR'd), or 0
on failure; call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_HapticEffectSupported]]
:[[SDL_HapticNumEffects]]

----
[[CategoryAPI]]


