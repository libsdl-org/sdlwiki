====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_IsScreenSaverEnabled =

Check whether the screensaver is currently enabled.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_IsScreenSaverEnabled(void);
</syntaxhighlight>

== Return Value ==

Returns [[SDL_TRUE]] if the screensaver is enabled, [[SDL_FALSE]] if it is
disabled.

== Remarks ==

The screensaver is disabled by default since SDL 2.0.2. Before SDL 2.0.2
the screensaver was enabled by default.

The default can also be changed using
<code>[[SDL_HINT_VIDEO_ALLOW_SCREENSAVER]]</code>.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_DisableScreenSaver]]
:[[SDL_EnableScreenSaver]]

----
[[CategoryAPI]]


