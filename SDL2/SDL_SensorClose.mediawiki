====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_SensorClose =

Close a sensor previously opened with [[SDL_SensorOpen]]().

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_SensorClose(SDL_Sensor *sensor);
</syntaxhighlight>

== Function Parameters ==

{|
|'''sensor'''
|The [[SDL_Sensor]] object to close
|}

== Version ==

This function is available since SDL 2.0.9.

----
[[CategoryAPI]]


