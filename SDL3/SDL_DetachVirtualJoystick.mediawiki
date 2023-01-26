====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_DetachVirtualJoystick =

Detach a virtual joystick.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_DetachVirtualJoystick(SDL_JoystickID instance_id);
</syntaxhighlight>

== Function Parameters ==

{|
|'''instance_id'''
|the joystick instance ID, previously returned from [[SDL_AttachVirtualJoystick]]()
|}

== Return Value ==

Returns 0 on success, or -1 if an error occurred.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


