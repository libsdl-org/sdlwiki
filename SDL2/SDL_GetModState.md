====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetModState =

Get the current key modifier state for the keyboard.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Keymod SDL_GetModState(void);
</syntaxhighlight>

== Return Value ==

Returns an OR'd combination of the modifier keys for the keyboard. See
[[SDL_Keymod]] for details.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetKeyboardState]]
:[[SDL_SetModState]]

----
[[CategoryAPI]]


