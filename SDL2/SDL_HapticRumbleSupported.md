====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HapticRumbleSupported =

Check whether rumble is supported on a haptic device.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_HapticRumbleSupported(SDL_Haptic * haptic);
</syntaxhighlight>

== Function Parameters ==

{|
|'''haptic'''
|haptic device to check for rumble support
|}

== Return Value ==

Returns [[SDL_TRUE]] if effect is supported, [[SDL_FALSE]] if it isn't, or
a negative error code on failure; call [[SDL_GetError]]() for more
information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_HapticRumbleInit]]
:[[SDL_HapticRumblePlay]]
:[[SDL_HapticRumbleStop]]

----
[[CategoryAPI]]


