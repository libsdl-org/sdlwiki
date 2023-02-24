====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_JoystickHasRumbleTriggers =

Query whether a joystick has rumble support on triggers.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_JoystickHasRumbleTriggers(SDL_Joystick *joystick);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|The joystick to query
|}

== Return Value ==

Return [[SDL_TRUE]] if the joystick has trigger rumble, [[SDL_FALSE]]
otherwise.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_RumbleJoystickTriggers]]

----
[[CategoryAPI]]


