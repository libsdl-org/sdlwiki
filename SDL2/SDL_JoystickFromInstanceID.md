====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickFromInstanceID =

Get the [[SDL_Joystick]] associated with an instance id.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Joystick* SDL_JoystickFromInstanceID(SDL_JoystickID instance_id);
</syntaxhighlight>

== Function Parameters ==

{|
|'''instance_id'''
|the instance id to get the [[SDL_Joystick]] for
|}

== Return Value ==

Returns an [[SDL_Joystick]] on success or NULL on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.4.

----
[[CategoryAPI]]


