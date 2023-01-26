====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetJoystickGUIDString =

Get an ASCII string representation for a given [[SDL_JoystickGUID]].

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_GetJoystickGUIDString(SDL_JoystickGUID guid, char *pszGUID, int cbGUID);
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

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetJoystickInstanceGUID]]
:[[SDL_GetJoystickGUID]]
:[[SDL_GetJoystickGUIDFromString]]

----
[[CategoryAPI]]


