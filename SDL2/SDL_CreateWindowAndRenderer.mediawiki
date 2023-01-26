====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_CreateWindowAndRenderer =

Create a window and default renderer.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_CreateWindowAndRenderer(
        int width, int height, Uint32 window_flags,
        SDL_Window **window, SDL_Renderer **renderer);
</syntaxhighlight>

== Function Parameters ==

{|
|'''width'''
|the width of the window
|-
|'''height'''
|the height of the window
|-
|'''window_flags'''
|the flags used to create the window (see [[SDL_CreateWindow]]())
|-
|'''window'''
|a pointer filled with the window, or NULL on error
|-
|'''renderer'''
|a pointer filled with the renderer, or NULL on error
|}

== Return Value ==

Returns 0 on success, or -1 on error; call [[SDL_GetError]]() for more
information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateRenderer]]
:[[SDL_CreateWindow]]

----
[[CategoryAPI]]


