====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerIsSensorEnabled =

Query whether sensor data reporting is enabled for a game controller.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_GameControllerIsSensorEnabled(SDL_GameController *gamecontroller, SDL_SensorType type);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamecontroller'''
|The controller to query
|-
|'''type'''
|The type of sensor to query
|}

== Return Value ==

Returns [[SDL_TRUE]] if the sensor is enabled, [[SDL_FALSE]] otherwise.

== Version ==

This function is available since SDL 2.0.14.

----
[[CategoryAPI]]


