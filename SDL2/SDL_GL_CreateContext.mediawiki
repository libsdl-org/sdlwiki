====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GL_CreateContext =

Create an OpenGL context for an OpenGL window, and make it current.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_GLContext SDL_GL_CreateContext(SDL_Window *
                                   window);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to associate with the context
|}

== Return Value ==

Returns the OpenGL context associated with <code>window</code> or NULL on
error; call [[SDL_GetError]]() for more details.

== Remarks ==

Windows users new to OpenGL should note that, for historical reasons, GL
functions added after OpenGL version 1.1 are not available by default.
Those functions must be loaded at run-time, either with an OpenGL
extension-handling library or with [[SDL_GL_GetProcAddress]]() and its
related functions.

[[SDL_GLContext]] is an alias for <code>void *</code>. It's opaque to the
application.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GL_DeleteContext]]
:[[SDL_GL_MakeCurrent]]

----
[[CategoryAPI]]


