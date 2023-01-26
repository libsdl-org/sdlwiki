====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerGetJoystick =

Get the Joystick ID from a Game Controller.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Joystick* SDL_GameControllerGetJoystick(SDL_GameController *gamecontroller);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamecontroller'''
|the game controller object that you want to get a joystick from
|}

== Return Value ==

Returns a [[SDL_Joystick]] object; call [[SDL_GetError]]() for more
information.

== Remarks ==

This function will give you a [[SDL_Joystick]] object, which allows you to
use the [[SDL_Joystick]] functions with a [[SDL_GameController]] object.
This would be useful for getting a joystick's position at any given time,
even if it hasn't moved (moving it would produce an event, which would have
the axis' value).

The pointer returned is owned by the [[SDL_GameController]]. You should not
call [[SDL_JoystickClose]]() on it, for example, since doing so will likely
cause SDL to crash.

== Version ==

This function is available since SDL 2.0.0.

----
[[CategoryAPI]]


