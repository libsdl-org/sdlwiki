====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickHasRumble =

Query whether a joystick has rumble support.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_JoystickHasRumble(SDL_Joystick *joystick);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|The joystick to query
|}

== Return Value ==

Return [[SDL_TRUE]] if the joystick has rumble, [[SDL_FALSE]] otherwise.

== Version ==

This function is available since SDL 2.0.18.

== Related Functions ==

:[[SDL_JoystickRumble]]

----
[[CategoryAPI]]


