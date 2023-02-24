====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetDisplayForPoint =

Get the display containing a point 

== Syntax ==

<syntaxhighlight lang='c'>
SDL_DisplayID SDL_GetDisplayForPoint(const SDL_Point *point);
</syntaxhighlight>

== Function Parameters ==

{|
|'''point'''
|the point to query
|}

== Return Value ==

Returns the instance ID of the display containing the point or 0 on
failure; call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetDisplayBounds]]
:[[SDL_GetDisplays]]

----
[[CategoryAPI]]


