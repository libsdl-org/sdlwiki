====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_SetWindowPosition =

Set the position of a window, in screen coordinates.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_SetWindowPosition(SDL_Window *window, int x, int y);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to reposition
|-
|'''x'''
|the x coordinate of the window, or <code>[[SDL_WINDOWPOS_CENTERED]]</code> or <code>[[SDL_WINDOWPOS_UNDEFINED]]</code>
|-
|'''y'''
|the y coordinate of the window, or <code>[[SDL_WINDOWPOS_CENTERED]]</code> or <code>[[SDL_WINDOWPOS_UNDEFINED]]</code>
|}

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetWindowPosition]]

----
[[CategoryAPI]], [[CategoryVideo]]


