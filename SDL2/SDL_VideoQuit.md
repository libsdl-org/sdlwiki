====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_VideoQuit =

Shut down the video subsystem, if initialized with [[SDL_VideoInit]]().

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_VideoQuit(void);
</syntaxhighlight>

== Remarks ==

This function closes all windows, and restores the original video mode.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_VideoInit]]

----
[[CategoryAPI]]


