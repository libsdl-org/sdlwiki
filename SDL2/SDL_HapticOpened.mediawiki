====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HapticOpened =

Check if the haptic device at the designated index has been opened.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_HapticOpened(int device_index);
</syntaxhighlight>

== Function Parameters ==

{|
|'''device_index'''
|the index of the device to query
|}

== Return Value ==

Returns 1 if it has been opened, 0 if it hasn't or on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_HapticIndex]]
:[[SDL_HapticOpen]]

----
[[CategoryAPI]]


