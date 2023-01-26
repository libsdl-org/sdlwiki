====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_CreateRenderer =

Create a 2D rendering context for a window.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Renderer * SDL_CreateRenderer(SDL_Window * window,
                       int index, Uint32 flags);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window where rendering is displayed
|-
|'''index'''
|the index of the rendering driver to initialize, or -1 to initialize the first one supporting the requested flags
|-
|'''flags'''
|0, or one or more [[SDL_RendererFlags]] OR'd together
|}

== Return Value ==

Returns a valid rendering context or NULL if there was an error; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateSoftwareRenderer]]
:[[SDL_DestroyRenderer]]
:[[SDL_GetNumRenderDrivers]]
:[[SDL_GetRendererInfo]]

----
[[CategoryAPI]]


