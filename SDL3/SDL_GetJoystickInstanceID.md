====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetJoystickInstanceID =

Get the instance ID of an opened joystick.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_JoystickID SDL_GetJoystickInstanceID(SDL_Joystick *joystick);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|an [[SDL_Joystick]] structure containing joystick information
|}

== Return Value ==

Returns the instance ID of the specified joystick on success or 0 on
failure; call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_OpenJoystick]]

----
[[CategoryAPI]]


