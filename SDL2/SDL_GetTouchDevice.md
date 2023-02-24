====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetTouchDevice =

Get the touch ID with the given index.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_TouchID SDL_GetTouchDevice(int index);
</syntaxhighlight>

== Function Parameters ==

{|
|'''index'''
|the touch device index
|}

== Return Value ==

Returns the touch ID with the given index on success or 0 if the index is
invalid; call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetNumTouchDevices]]

----
[[CategoryAPI]]


