====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_SetMainReady =

Circumvent failure of [[SDL_Init]]() when not using [[SDL_main]]() as an entry point.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_SetMainReady(void);
</syntaxhighlight>

== Remarks ==

This function is defined in [[SDL_main]].h, along with the preprocessor
rule to redefine main() as [[SDL_main]](). Thus to ensure that your main()
function will not be changed it is necessary to define [[SDL_MAIN_HANDLED]]
before including SDL.h.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_Init]]

----
[[CategoryAPI]]


