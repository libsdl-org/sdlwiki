====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_JoystickGetGUIDString =

Get an ASCII string representation for a given [[SDL_JoystickGUID]].

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_JoystickGetGUIDString(SDL_JoystickGUID guid, char *pszGUID, int cbGUID);
</syntaxhighlight>

== Function Parameters ==

{|
|'''guid'''
|the [[SDL_JoystickGUID]] you wish to convert to string
|-
|'''pszGUID'''
|buffer in which to write the ASCII string
|-
|'''cbGUID'''
|the size of pszGUID
|}

== Remarks ==

You should supply at least 33 bytes for pszGUID.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_JoystickGetDeviceGUID]]
:[[SDL_JoystickGetGUID]]
:[[SDL_JoystickGetGUIDFromString]]

----
[[CategoryAPI]]


