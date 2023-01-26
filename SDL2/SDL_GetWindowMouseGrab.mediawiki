====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetWindowMouseGrab =

Get a window's mouse grab mode.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_GetWindowMouseGrab(SDL_Window * window);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to query
|}

== Return Value ==

Returns [[SDL_TRUE]] if mouse is grabbed, and [[SDL_FALSE]] otherwise.

== Version ==

This function is available since SDL 2.0.16.

== Related Functions ==

:[[SDL_SetWindowKeyboardGrab]]
:[[SDL_GetWindowGrab]]

----
[[CategoryAPI]]


