====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickGetAttached =

Get the status of a specified joystick.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_JoystickGetAttached(SDL_Joystick *joystick);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|the joystick to query
|}

== Return Value ==

Returns [[SDL_TRUE]] if the joystick has been opened, [[SDL_FALSE]] if it
has not; call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_JoystickClose]]
:[[SDL_JoystickOpen]]

----
[[CategoryAPI]]


