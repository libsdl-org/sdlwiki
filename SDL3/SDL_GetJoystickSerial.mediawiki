====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetJoystickSerial =

Get the serial number of an opened joystick, if available.

== Syntax ==

<syntaxhighlight lang='c'>
const char * SDL_GetJoystickSerial(SDL_Joystick *joystick);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|the [[SDL_Joystick]] obtained from [[SDL_OpenJoystick]]()
|}

== Return Value ==

Returns the serial number of the selected joystick, or NULL if unavailable.

== Remarks ==

Returns the serial number of the joystick, or NULL if it is not available.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


