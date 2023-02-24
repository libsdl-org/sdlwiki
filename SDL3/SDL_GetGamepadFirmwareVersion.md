====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetGamepadFirmwareVersion =

Get the firmware version of an opened gamepad, if available.

== Syntax ==

<syntaxhighlight lang='c'>
Uint16 SDL_GetGamepadFirmwareVersion(SDL_Gamepad *gamepad);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamepad'''
|the gamepad object to query.
|}

== Return Value ==

Return the gamepad firmware version, or zero if unavailable.

== Remarks ==

If the firmware version isn't available this function returns 0.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


