====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_ShowWindow =

Show a window.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_ShowWindow(SDL_Window *window);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to show
|}

== Version ==

This function is available since SDL 3.0.0.

== Code Examples ==

<syntaxhighlight lang='c++'>
SDL_ShowWindow(window);
</syntaxhighlight>

== Related Functions ==

:[[SDL_HideWindow]]
:[[SDL_RaiseWindow]]

----
[[CategoryAPI]], [[CategoryVideo]]


