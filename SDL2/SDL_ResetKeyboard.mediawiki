====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_ResetKeyboard =

Clear the state of the keyboard 

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_ResetKeyboard(void);
</syntaxhighlight>

== Remarks ==

This function will generate key up events for all pressed keys.

== Version ==

This function is available since SDL 2.24.0.

== Related Functions ==

:[[SDL_GetKeyboardState]]

----
[[CategoryAPI]]


