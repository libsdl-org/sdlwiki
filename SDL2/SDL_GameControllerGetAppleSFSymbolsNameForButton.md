====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GameControllerGetAppleSFSymbolsNameForButton =

Return the sfSymbolsName for a given button on a game controller on Apple platforms.

== Syntax ==

<syntaxhighlight lang='c'>
const char* SDL_GameControllerGetAppleSFSymbolsNameForButton(SDL_GameController *gamecontroller, SDL_GameControllerButton button);
</syntaxhighlight>

== Function Parameters ==

{|
|'''gamecontroller'''
|the controller to query
|-
|'''button'''
|a button on the game controller
|}

== Return Value ==

Returns the sfSymbolsName or NULL if the name can't be found

== Version ==

This function is available since SDL 2.0.18.

== Related Functions ==

:[[SDL_GameControllerGetAppleSFSymbolsNameForAxis]]

----
[[CategoryAPI]]


