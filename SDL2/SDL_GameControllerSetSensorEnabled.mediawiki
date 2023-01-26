====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerSetSensorEnabled =

Set whether data reporting for a game controller sensor is enabled.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GameControllerSetSensorEnabled(SDL_GameController *gamecontroller, SDL_SensorType type, SDL_bool enabled);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamecontroller'''
|The controller to update
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

This function is available since SDL 2.0.14.

----
[[CategoryAPI]]


