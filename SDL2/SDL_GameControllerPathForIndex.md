====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerPathForIndex =

Get the implementation dependent path for the game controller.

== Syntax ==

<syntaxhighlight lang='c'>
const char* SDL_GameControllerPathForIndex(int joystick_index);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joystick_index'''
|the device_index of a device, from zero to [[SDL_NumJoysticks]]()-1
|}

== Return Value ==

Returns the implementation-dependent path for the game controller, or NULL
if there is no path or the index is invalid.

== Remarks ==

This function can be called before any controllers are opened.

<code>joystick_index</code> is the same as the <code>device_index</code>
passed to [[SDL_JoystickOpen]]().

== Version ==

This function is available since SDL 2.24.0.

== Related Functions ==

:[[SDL_GameControllerPath]]

----
[[CategoryAPI]]


