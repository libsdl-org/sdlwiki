====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_EGL_GetCurrentEGLConfig =

Get the currently active EGL config.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_EGLConfig SDL_EGL_GetCurrentEGLConfig(void);
</syntaxhighlight>

== Return Value ==

Returns the currently active EGL config or NULL on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


