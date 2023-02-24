====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GL_GetAttribute =

Get the actual value for an attribute from the current context.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GL_GetAttribute(SDL_GLattr attr, int *value);
</syntaxhighlight>

== Function Parameters ==

{|
|'''attr'''
|an [[SDL_GLattr]] enum value specifying the OpenGL attribute to get
|-
|'''value'''
|a pointer filled in with the current value of <code>attr</code>
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GL_ResetAttributes]]
:[[SDL_GL_SetAttribute]]

----
[[CategoryAPI]]


