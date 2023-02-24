====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickGetType =

Get the type of an opened joystick.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_JoystickType SDL_JoystickGetType(SDL_Joystick *joystick);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick'''
|the [[SDL_Joystick]] obtained from [[SDL_JoystickOpen]]()
|}

== Return Value ==

Returns the [[SDL_JoystickType]] of the selected joystick.

== Version ==

This function is available since SDL 2.0.6.

----
[[CategoryAPI]]


