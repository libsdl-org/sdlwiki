====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GL_LoadLibrary =

Dynamically load an OpenGL library.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GL_LoadLibrary(const char *path);
</syntaxhighlight>

== Function Parameters ==

{|
|'''path'''
|the platform dependent OpenGL library name, or NULL to open the default OpenGL library
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

This should be done after initializing the video driver, but before
creating any OpenGL windows. If no OpenGL library is loaded, the default
library will be loaded upon creation of the first OpenGL window.

If you do this, you need to retrieve all of the GL functions used in your
program from the dynamic library using [[SDL_GL_GetProcAddress]]().

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GL_GetProcAddress]]
:[[SDL_GL_UnloadLibrary]]

----
[[CategoryAPI]], [[CategoryVideo]]


