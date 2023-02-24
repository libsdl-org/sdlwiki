====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerGetButtonFromString =

Convert a string into an [[SDL_GameControllerButton]] enum.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_GameControllerButton SDL_GameControllerGetButtonFromString(const char *str);
</syntaxhighlight>

== Function Parameters ==

{|
|'''str'''
|string representing a [[SDL_GameController]] axis
|}

== Return Value ==

Returns the [[SDL_GameControllerButton]] enum corresponding to the input
string, or <code>[[SDL_CONTROLLER_AXIS_INVALID]]</code> if no match was
found.

== Remarks ==

This function is called internally to translate [[SDL_GameController]]
mapping strings for the underlying joystick device into the consistent
[[SDL_GameController]] mapping. You do not normally need to call this
function unless you are parsing [[SDL_GameController]] mappings in your own
code.

== Version ==

This function is available since SDL 2.0.0.

----
[[CategoryAPI]]


