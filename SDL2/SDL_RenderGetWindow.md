====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RenderGetWindow =

Get the window associated with a renderer.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Window * SDL_RenderGetWindow(SDL_Renderer *renderer);
</syntaxhighlight>

== Function Parameters ==

{|
|'''renderer'''
|the renderer to query
|}

== Return Value ==

Returns the window on success or NULL on failure; call [[SDL_GetError]]()
for more information.

== Version ==

This function is available since SDL 2.0.22.

----
[[CategoryAPI]]


