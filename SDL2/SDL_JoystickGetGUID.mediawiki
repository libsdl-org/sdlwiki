====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickGetGUID =

Get the implementation-dependent GUID for the joystick.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_JoystickGUID SDL_JoystickGetGUID(SDL_Joystick *joystick);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|the [[SDL_Joystick]] obtained from [[SDL_JoystickOpen]]()
|}

== Return Value ==

Returns the GUID of the given joystick. If called on an invalid index, this
function returns a zero GUID; call [[SDL_GetError]]() for more information.

== Remarks ==

This function requires an open joystick.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_JoystickGetDeviceGUID]]
:[[SDL_JoystickGetGUIDString]]

----
[[CategoryAPI]]


