====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetDisplayMode =

Get information about a specific display mode.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GetDisplayMode(int displayIndex, int modeIndex,
                       SDL_DisplayMode * mode);
</syntaxhighlight>

== Function Parameters ==

{|
|'''displayIndex'''
|the index of the display to query
|-
|'''modeIndex'''
|the index of the display mode to query
|-
|'''mode'''
|an [[SDL_DisplayMode]] structure filled in with the mode at <code>modeIndex</code>
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

The display modes are sorted in this priority:

* width -> largest to smallest
* height -> largest to smallest
* bits per pixel -> more colors to fewer colors
* packed pixel layout -> largest to smallest
* refresh rate -> highest to lowest

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetNumDisplayModes]]

----
[[CategoryAPI]]


