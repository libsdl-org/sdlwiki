====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HapticNumEffects =

Get the number of effects a haptic device can store.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_HapticNumEffects(SDL_Haptic * haptic);
</syntaxhighlight>

== Function Parameters ==

{|
|'''haptic'''
|the [[SDL_Haptic]] device to query
|}

== Return Value ==

Returns the number of effects the haptic device can store or a negative
error code on failure; call [[SDL_GetError]]() for more information.

== Remarks ==

On some platforms this isn't fully supported, and therefore is an
approximation. Always check to see if your created effect was actually
created and do not rely solely on [[SDL_HapticNumEffects]]().

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_HapticNumEffectsPlaying]]
:[[SDL_HapticQuery]]

----
[[CategoryAPI]]


