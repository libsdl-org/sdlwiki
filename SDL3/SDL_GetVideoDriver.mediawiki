====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetVideoDriver =

Get the name of a built in video driver.

== Syntax ==

<syntaxhighlight lang='c'>
const char* SDL_GetVideoDriver(int index);
</syntaxhighlight>

== Function Parameters ==

{|
|'''index'''
|the index of a video driver
|}

== Return Value ==

Returns the name of the video driver with the given '''index'''.

== Remarks ==

The video drivers are presented in the order in which they are normally
checked during initialization.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetNumVideoDrivers]]

----
[[CategoryAPI]], [[CategoryVideo]]


