====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_SetWindowMouseGrab =

Set a window's mouse grab mode.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_SetWindowMouseGrab(SDL_Window * window,
                            SDL_bool grabbed);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|The window for which the mouse grab mode should be set.
|-
|'''grabbed'''
|This is [[SDL_TRUE]] to grab mouse, and [[SDL_FALSE]] to release.
|}

== Remarks ==

Mouse grab confines the mouse cursor to the window.

== Version ==

This function is available since SDL 2.0.16.

== Related Functions ==

:[[SDL_GetWindowMouseGrab]]
:[[SDL_SetWindowKeyboardGrab]]
:[[SDL_SetWindowGrab]]

----
[[CategoryAPI]]


