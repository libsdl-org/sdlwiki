====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerGetVendor =

Get the USB vendor ID of an opened controller, if available.

== Syntax ==

<syntaxhighlight lang='c'>
Uint16 SDL_GameControllerGetVendor(SDL_GameController *gamecontroller);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamecontroller'''
|the game controller object to query.
|}

== Return Value ==

Return the USB vendor ID, or zero if unavailable.

== Remarks ==

If the vendor ID isn't available this function returns 0.

== Version ==

This function is available since SDL 2.0.6.

----
[[CategoryAPI]]


