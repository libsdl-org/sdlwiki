====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GamepadHasRumble =

Query whether a gamepad has rumble support.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_GamepadHasRumble(SDL_Gamepad *gamepad);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamepad'''
|The gamepad to query
|}

== Return Value ==

Returns [[SDL_TRUE]], or [[SDL_FALSE]] if this gamepad does not have rumble
support

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_RumbleGamepad]]

----
[[CategoryAPI]]


