====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HapticNumEffectsPlaying =

Get the number of effects a haptic device can play at the same time.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_HapticNumEffectsPlaying(SDL_Haptic * haptic);
</syntaxhighlight>

== Function Parameters ==

{|
|'''haptic'''
|the [[SDL_Haptic]] device to query maximum playing effects
|}

== Return Value ==

Returns the number of effects the haptic device can play at the same time
or a negative error code on failure; call [[SDL_GetError]]() for more
information.

== Remarks ==

This is not supported on all platforms, but will always return a value.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_HapticNumEffects]]
:[[SDL_HapticQuery]]

----
[[CategoryAPI]]


