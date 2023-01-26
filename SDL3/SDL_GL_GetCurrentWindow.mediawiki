====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======

== Draft ==

'''THIS PAGE IS A WORK IN PROGRESS''' ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGFunctions for details on editing this page*^*^*^*^* -->
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

This function is available since SDL 3.0.0.

----
[[CategoryAPI]], [[CategoryVideo]], [[CategoryDraft]]


