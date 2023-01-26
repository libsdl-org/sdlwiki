====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_CreateWindowFrom =

Create an SDL window from an existing native window.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Window * SDL_CreateWindowFrom(const void *data);
</syntaxhighlight>

== Function Parameters ==

{|
|'''data'''
|a pointer to driver-dependent window creation data, typically your native window cast to a void*
|}

== Return Value ==

Returns the window that was created or NULL on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

In some cases (e.g. OpenGL) and on some platforms (e.g. Microsoft Windows)
the hint <code>[[SDL_HINT_VIDEO_WINDOW_SHARE_PIXEL_FORMAT]]</code> needs to
be configured before using [[SDL_CreateWindowFrom]]().

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateWindow]]
:[[SDL_DestroyWindow]]

----
[[CategoryAPI]]


