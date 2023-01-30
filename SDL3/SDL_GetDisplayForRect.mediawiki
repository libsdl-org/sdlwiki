====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetDisplayForRect =

Get the display primarily containing a rect 

== Syntax ==

<syntaxhighlight lang='c'>
SDL_DisplayID SDL_GetDisplayForRect(const SDL_Rect *rect);
</syntaxhighlight>

== Function Parameters ==

{|
|'''rect'''
|the rect to query
|}

== Return Value ==

Returns the instance ID of the display entirely containing the rect or
closest to the center of the rect on success or 0 on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetDisplayBounds]]
:[[SDL_GetDisplays]]

----
[[CategoryAPI]]


