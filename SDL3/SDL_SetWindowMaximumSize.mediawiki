====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_SetWindowMaximumSize =

Set the maximum size of a window's client area, in screen coordinates.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_SetWindowMaximumSize(SDL_Window *window, int max_w, int max_h);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to change
|-
|'''max_w'''
|the maximum width of the window
|-
|'''max_h'''
|the maximum height of the window
|}

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetWindowMaximumSize]]
:[[SDL_SetWindowMinimumSize]]

----
[[CategoryAPI]], [[CategoryVideo]]
<!-- #See the Style Guide for instructions on editing the footer. -->


