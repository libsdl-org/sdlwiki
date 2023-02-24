====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_JoystickConnected =

Get the status of a specified joystick.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_JoystickConnected(SDL_Joystick *joystick);
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

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_CloseJoystick]]
:[[SDL_OpenJoystick]]

----
[[CategoryAPI]]


