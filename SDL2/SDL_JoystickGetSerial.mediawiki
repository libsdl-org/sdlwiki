====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickGetSerial =

Get the serial number of an opened joystick, if available.

== Syntax ==

<syntaxhighlight lang='c'>
const char * SDL_JoystickGetSerial(SDL_Joystick *joystick);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|the [[SDL_Joystick]] obtained from [[SDL_JoystickOpen]]()
|}

== Return Value ==

Returns the serial number of the selected joystick, or NULL if unavailable.

== Remarks ==

Returns the serial number of the joystick, or NULL if it is not available.

== Version ==

This function is available since SDL 2.0.14.

----
[[CategoryAPI]]


