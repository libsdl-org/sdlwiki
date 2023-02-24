====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetJoystickType =

Get the type of an opened joystick.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_JoystickType SDL_GetJoystickType(SDL_Joystick *joystick);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|the [[SDL_Joystick]] obtained from [[SDL_OpenJoystick]]()
|}

== Return Value ==

Returns the [[SDL_JoystickType]] of the selected joystick.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


