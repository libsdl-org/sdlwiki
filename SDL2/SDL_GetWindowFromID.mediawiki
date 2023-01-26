====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetWindowFromID =

Get a window from a stored ID.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Window * SDL_GetWindowFromID(Uint32 id);
</syntaxhighlight>

== Function Parameters ==

{|
|'''id'''
|the ID of the window
|}

== Return Value ==

Returns the window associated with <code>id</code> or NULL if it doesn't
exist; call [[SDL_GetError]]() for more information.

== Remarks ==

The numeric ID is what [[SDL_WindowEvent]] references, and is necessary to
map these events to specific [[SDL_Window]] objects.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetWindowID]]

----
[[CategoryAPI]]


