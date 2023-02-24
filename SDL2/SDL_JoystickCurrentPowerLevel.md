====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickCurrentPowerLevel =

Get the battery level of a joystick as [[SDL_JoystickPowerLevel]].

== Syntax ==

<syntaxhighlight lang='c'>
SDL_JoystickPowerLevel SDL_JoystickCurrentPowerLevel(SDL_Joystick *joystick);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|the [[SDL_Joystick]] to query
|}

== Return Value ==

Returns the current battery level as [[SDL_JoystickPowerLevel]] on success
or <code>[[SDL_JOYSTICK_POWER_UNKNOWN]]</code> if it is unknown

== Version ==

This function is available since SDL 2.0.4.

----
[[CategoryAPI]]


