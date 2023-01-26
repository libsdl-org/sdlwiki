====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetDisplayBounds =

Get the desktop area represented by a display.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GetDisplayBounds(int displayIndex, SDL_Rect * rect);
</syntaxhighlight>

== Function Parameters ==

{|
|'''displayIndex'''
|the index of the display to query
|-
|'''rect'''
|the [[SDL_Rect]] structure filled in with the display bounds
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

The primary display (<code>displayIndex</code> zero) is always located at
0,0.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetNumVideoDisplays]]

----
[[CategoryAPI]]


