====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetGamepadProductVersion =

Get the product version of an opened gamepad, if available.

== Syntax ==

<syntaxhighlight lang='c'>
Uint16 SDL_GetGamepadProductVersion(SDL_Gamepad *gamepad);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamepad'''
|the gamepad object to query.
|}

== Return Value ==

Return the USB product version, or zero if unavailable.

== Remarks ==

If the product version isn't available this function returns 0.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


