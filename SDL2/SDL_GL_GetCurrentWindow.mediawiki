====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GL_GetCurrentWindow =

Get the currently active OpenGL window.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Window* SDL_GL_GetCurrentWindow(void);
</syntaxhighlight>

== Return Value ==

Returns the currently active OpenGL window on success or NULL on failure;
call [[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

----
[[CategoryAPI]]


