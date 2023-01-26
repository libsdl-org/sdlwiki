====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerGetFirmwareVersion =

Get the firmware version of an opened controller, if available.

== Syntax ==

<syntaxhighlight lang='c'>
Uint16 SDL_GameControllerGetFirmwareVersion(SDL_GameController *gamecontroller);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamecontroller'''
|the game controller object to query.
|}

== Return Value ==

Return the controller firmware version, or zero if unavailable.

== Remarks ==

If the firmware version isn't available this function returns 0.

== Version ==

This function is available since SDL 2.24.0.

----
[[CategoryAPI]]


