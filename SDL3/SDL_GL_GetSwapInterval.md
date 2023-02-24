====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GL_GetSwapInterval =

Get the swap interval for the current OpenGL context.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GL_GetSwapInterval(int *interval);
</syntaxhighlight>

== Function Parameters ==

{|
|'''interval'''
|Output interval value. 0 if there is no vertical retrace synchronization, 1 if the buffer swap is synchronized with the vertical retrace, and -1 if late swaps happen immediately instead of waiting for the next retrace
|}

== Return Value ==

Returns 0 on success or -1 error. call [[SDL_GetError]]() for more
information.

== Remarks ==

If the system can't determine the swap interval, or there isn't a valid
current context, this function will set *interval to 0 as a safe default.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GL_SetSwapInterval]]

----
[[CategoryAPI]], [[CategoryVideo]]


