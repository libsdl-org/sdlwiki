====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerFromInstanceID =

Get the [[SDL_GameController]] associated with an instance id.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_GameController* SDL_GameControllerFromInstanceID(SDL_JoystickID joyid);
</syntaxhighlight>

== Function Parameters ==

{|
|'''joyid'''
|the instance id to get the [[SDL_GameController]] for
|}

== Return Value ==

Returns an [[SDL_GameController]] on success or NULL on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.4.

----
[[CategoryAPI]]


