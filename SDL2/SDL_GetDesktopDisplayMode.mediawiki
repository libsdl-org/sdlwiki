====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetDesktopDisplayMode =

Get information about the desktop's display mode.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GetDesktopDisplayMode(int displayIndex, SDL_DisplayMode * mode);
</syntaxhighlight>

== Function Parameters ==

{|
|'''displayIndex'''
|the index of the display to query
|-
|'''mode'''
|an [[SDL_DisplayMode]] structure filled in with the current display mode
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

There's a difference between this function and
[[SDL_GetCurrentDisplayMode]]() when SDL runs fullscreen and has changed
the resolution. In that case this function will return the previous native
display mode, and not the current display mode.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetCurrentDisplayMode]]
:[[SDL_GetDisplayMode]]
:[[SDL_SetWindowDisplayMode]]

----
[[CategoryAPI]]


