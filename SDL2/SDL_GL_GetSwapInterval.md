====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GL_GetSwapInterval =

Get the swap interval for the current OpenGL context.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GL_GetSwapInterval(void);
</syntaxhighlight>

== Return Value ==

Returns 0 if there is no vertical retrace synchronization, 1 if the buffer
swap is synchronized with the vertical retrace, and -1 if late swaps happen
immediately instead of waiting for the next retrace; call
[[SDL_GetError]]() for more information.

== Remarks ==

If the system can't determine the swap interval, or there isn't a valid
current context, this function will return 0 as a safe default.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GL_SetSwapInterval]]

----
[[CategoryAPI]]


