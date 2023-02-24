====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_SetGamepadSensorEnabled =

Set whether data reporting for a gamepad sensor is enabled.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SetGamepadSensorEnabled(SDL_Gamepad *gamepad, SDL_SensorType type, SDL_bool enabled);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamepad'''
|The gamepad to update
|-
|'''type'''
|The type of sensor to enable/disable
|-
|'''enabled'''
|Whether data reporting should be enabled
|}

== Return Value ==

Returns 0 or -1 if an error occurred.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


