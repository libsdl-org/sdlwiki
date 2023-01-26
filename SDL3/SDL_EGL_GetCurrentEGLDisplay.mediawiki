====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_EGL_GetCurrentEGLDisplay =

Get the currently active EGL display.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_EGLDisplay SDL_EGL_GetCurrentEGLDisplay(void);
</syntaxhighlight>

== Return Value ==

Returns the currently active EGL display or NULL on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


