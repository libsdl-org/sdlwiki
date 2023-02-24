====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickIsVirtual =

Query whether or not the joystick at a given device index is virtual.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_JoystickIsVirtual(int device_index);
</syntaxhighlight>

== Function Parameters ==

{|
|'''device_index'''
|a joystick device index.
|}

== Return Value ==

Returns [[SDL_TRUE]] if the joystick is virtual, [[SDL_FALSE]] otherwise.

== Version ==

This function is available since SDL 2.0.14.

----
[[CategoryAPI]]


