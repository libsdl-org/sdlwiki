====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetSensorNonPortableType =

Get the platform dependent type of a sensor.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GetSensorNonPortableType(SDL_Sensor *sensor);
</syntaxhighlight>

== Function Parameters ==

{|
|'''sensor'''
|The [[SDL_Sensor]] object to inspect
|}

== Return Value ==

Returns the sensor platform dependent type, or -1 if <code>sensor</code> is
NULL.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


