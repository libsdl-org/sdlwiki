====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerMappingForGUID =

Get the game controller mapping string for a given GUID.

== Syntax ==

<syntaxhighlight lang='c'>
char * SDL_GameControllerMappingForGUID(SDL_JoystickGUID guid);
</syntaxhighlight>

== Function Parameters ==

{|
|'''guid'''
|a structure containing the GUID for which a mapping is desired
|}

== Return Value ==

Returns a mapping string or NULL on error; call [[SDL_GetError]]() for more
information.

== Remarks ==

The returned string must be freed with [[SDL_free]]().

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_JoystickGetDeviceGUID]]
:[[SDL_JoystickGetGUID]]

----
[[CategoryAPI]]


