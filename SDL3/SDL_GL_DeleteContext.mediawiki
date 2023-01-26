====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_GL_DeleteContext =

Delete an OpenGL context.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_GL_DeleteContext(SDL_GLContext context);
</syntaxhighlight>

== Function Parameters ==

{|
|'''context'''
|the OpenGL context to be deleted
|}

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_GL_CreateContext]]

----
[[CategoryAPI]], [[CategoryVideo]]


