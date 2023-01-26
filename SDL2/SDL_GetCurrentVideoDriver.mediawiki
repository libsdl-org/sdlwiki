====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetCurrentVideoDriver =

Get the name of the currently initialized video driver.

== Syntax ==

<syntaxhighlight lang='c'>
const char* SDL_GetCurrentVideoDriver(void);
</syntaxhighlight>

== Return Value ==

Returns the name of the current video driver or NULL if no driver has been
initialized.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetNumVideoDrivers]]
:[[SDL_GetVideoDriver]]

----
[[CategoryAPI]]


