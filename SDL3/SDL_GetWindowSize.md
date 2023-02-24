====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetWindowSize =

Get the size of a window's client area, in screen coordinates.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_GetWindowSize(SDL_Window *window, int *w, int *h);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to query the width and height from
|-
|'''w'''
|a pointer filled in with the width of the window, may be NULL
|-
|'''h'''
|a pointer filled in with the height of the window, may be NULL
|}

== Remarks ==

NULL can safely be passed as the <code>w</code> or <code>h</code> parameter
if the width or height value is not desired.

The window size in screen coordinates may differ from the size in pixels if
the window is on a high density display (one with an OS scaling factor).
Use [[SDL_GetWindowSizeInPixels]]() or [[SDL_GetRendererOutputSize]]() to
get the real client area size in pixels.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetWindowSizeInPixels]]
:[[SDL_GetRendererOutputSize]]
:[[SDL_SetWindowSize]]

----
[[CategoryAPI]], [[CategoryVideo]]


