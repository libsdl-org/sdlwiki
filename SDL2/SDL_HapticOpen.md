====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HapticOpen =

Open a haptic device for use.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Haptic* SDL_HapticOpen(int device_index);
</syntaxhighlight>

== Function Parameters ==

{|
|'''device_index'''
|index of the device to open
|}

== Return Value ==

Returns the device identifier or NULL on failure; call [[SDL_GetError]]()
for more information.

== Remarks ==

The index passed as an argument refers to the N'th haptic device on this
system.

When opening a haptic device, its gain will be set to maximum and
autocenter will be disabled. To modify these values use
[[SDL_HapticSetGain]]() and [[SDL_HapticSetAutocenter]]().

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_HapticClose]]
:[[SDL_HapticIndex]]
:[[SDL_HapticOpenFromJoystick]]
:[[SDL_HapticOpenFromMouse]]
:[[SDL_HapticPause]]
:[[SDL_HapticSetAutocenter]]
:[[SDL_HapticSetGain]]
:[[SDL_HapticStopAll]]

----
[[CategoryAPI]]


