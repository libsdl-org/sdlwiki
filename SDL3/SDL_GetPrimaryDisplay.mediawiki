====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GetPrimaryDisplay =

Return the primary display.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_DisplayID SDL_GetPrimaryDisplay(void);
</syntaxhighlight>

== Return Value ==

Returns the instance ID of the primary display on success or 0 on failure;
call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GetDisplays]]

----
[[CategoryAPI]]


