====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_WarpMouseInWindow =

Move the mouse cursor to the given position within the window.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_WarpMouseInWindow(SDL_Window * window,
                           int x, int y);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to move the mouse into, or NULL for the current mouse focus
|-
|'''x'''
|the x coordinate within the window
|-
|'''y'''
|the y coordinate within the window
|}

== Remarks ==

This function generates a mouse motion event if relative mode is not
enabled. If relative mode is enabled, you can force mouse events for the
warp by setting the [[SDL_HINT_MOUSE_RELATIVE_WARP_MOTION]] hint.

Note that this function will appear to succeed, but not actually move the
mouse when used over Microsoft Remote Desktop.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_WarpMouseGlobal]]

----
[[CategoryAPI]]


