====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerFromPlayerIndex =

Get the [[SDL_GameController]] associated with a player index.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_GameController* SDL_GameControllerFromPlayerIndex(int player_index);
</syntaxhighlight>

== Function Parameters ==

{|
|'''player_index'''
|the player index, which is not the device index or the instance id!
|}

== Return Value ==

Returns the [[SDL_GameController]] associated with a player index.

== Remarks ==

Please note that the player index is _not_ the device index, nor is it the
instance id!

== Version ==

This function is available since SDL 2.0.12.

== Related Functions ==

:[[SDL_GameControllerGetPlayerIndex]]
:[[SDL_GameControllerSetPlayerIndex]]

----
[[CategoryAPI]]


