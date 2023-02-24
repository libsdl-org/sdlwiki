====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickGetDeviceGUID =

Get the implementation-dependent GUID for the joystick at a given device index.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_JoystickGUID SDL_JoystickGetDeviceGUID(int device_index);
</syntaxhighlight>

== Function Parameters ==

{|
|'''device_index'''
|the index of the joystick to query (the N'th joystick on the system
|}

== Return Value ==

Returns the GUID of the selected joystick. If called on an invalid index,
this function returns a zero GUID

== Remarks ==

This function can be called before any joysticks are opened.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_JoystickGetGUID]]
:[[SDL_JoystickGetGUIDString]]

----
[[CategoryAPI]]


