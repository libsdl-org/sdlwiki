====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerGetSensorDataWithTimestamp =

Get the current state of a game controller sensor with the timestamp of the last update.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GameControllerGetSensorDataWithTimestamp(SDL_GameController *gamecontroller, SDL_SensorType type, Uint64 *timestamp, float *data, int num_values);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamecontroller'''
|The controller to query
|-
|'''type'''
|The type of sensor to query
|-
|'''timestamp'''
|A pointer filled with the timestamp in microseconds of the current sensor reading if available, or 0 if not
|-
|'''data'''
|A pointer filled with the current sensor state
|-
|'''num_values'''
|The number of values to write to data
|}

== Return Value ==

Return 0 or -1 if an error occurred.

== Remarks ==

The number of values and interpretation of the data is sensor dependent.
See [[SDL_sensor]].h for the details for each type of sensor.

== Version ==

This function is available since SDL 2.26.0.

----
[[CategoryAPI]]


