====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetWindowFlags =

Get the window flags.

== Syntax ==

<syntaxhighlight lang='c'>
Uint32 SDL_GetWindowFlags(SDL_Window * window);
</syntaxhighlight>

== Function Parameters ==

{|
|'''window'''
|the window to query
|}

== Return Value ==

Returns a mask of the [[SDL_WindowFlags]] associated with
<code>window</code>

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateWindow]]
:[[SDL_HideWindow]]
:[[SDL_MaximizeWindow]]
:[[SDL_MinimizeWindow]]
:[[SDL_SetWindowFullscreen]]
:[[SDL_SetWindowGrab]]
:[[SDL_ShowWindow]]

----
[[CategoryAPI]]


