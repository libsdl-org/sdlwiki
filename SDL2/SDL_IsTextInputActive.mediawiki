====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_IsTextInputActive =

Check whether or not Unicode text input events are enabled.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_IsTextInputActive(void);
</syntaxhighlight>

== Return Value ==

Returns [[SDL_TRUE]] if text input events are enabled else [[SDL_FALSE]].

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_StartTextInput]]

----
[[CategoryAPI]]


