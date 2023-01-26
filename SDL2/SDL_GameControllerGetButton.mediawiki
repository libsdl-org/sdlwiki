====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerGetButton =

Get the current state of a button on a game controller.

== Syntax ==

<syntaxhighlight lang='c'>
Uint8 SDL_GameControllerGetButton(SDL_GameController *gamecontroller,
                                  SDL_GameControllerButton button);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamecontroller'''
|a game controller
|-
|'''button'''
|a button index (one of the [[SDL_GameControllerButton]] values)
|}

== Return Value ==

Returns 1 for pressed state or 0 for not pressed state or error; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GameControllerGetAxis]]

----
[[CategoryAPI]]


