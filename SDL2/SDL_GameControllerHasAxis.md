====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerHasAxis =

Query whether a game controller has a given axis.

== Syntax ==

<syntaxhighlight lang='c'>
extern DECLSPEC SDL_bool SDLCALL
SDL_GameControllerHasAxis(SDL_GameController *gamecontroller, SDL_GameControllerAxis axis);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamecontroller'''
|a game controller
|-
|'''axis'''
|an axis enum value (an [[SDL_GameControllerAxis]] value)
|}

== Return Value ==

Returns [[SDL_TRUE]] if the controller has this axis, [[SDL_FALSE]]
otherwise.

== Remarks ==

This merely reports whether the controller's mapping defined this axis, as
that is all the information SDL has about the physical device.

== Version ==

This function is available since SDL 2.0.14.

----
[[CategoryAPI]]


