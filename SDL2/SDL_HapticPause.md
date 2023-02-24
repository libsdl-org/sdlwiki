====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HapticPause =

Pause a haptic device.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_HapticPause(SDL_Haptic * haptic);
</syntaxhighlight>

== Function Parameters ==

{|
|'''haptic'''
|the [[SDL_Haptic]] device to pause
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

Device must support the <code>[[SDL_HAPTIC_PAUSE]]</code> feature. Call
[[SDL_HapticUnpause]]() to resume playback.

Do not modify the effects nor add new ones while the device is paused. That
can cause all sorts of weird errors.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_HapticUnpause]]

----
[[CategoryAPI]]


