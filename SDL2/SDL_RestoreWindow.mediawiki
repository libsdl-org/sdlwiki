====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RestoreWindow =

Restore the size and position of a minimized or maximized window.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_RestoreWindow(SDL_Window * window);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to restore
|}

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_MaximizeWindow]]
:[[SDL_MinimizeWindow]]

----
[[CategoryAPI]]


