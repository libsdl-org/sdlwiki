====== (This function is part of SDL_image, a separate library from SDL.) ======
= IMG_ReadXPMFromArray =

Load an XPM image from a memory array.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Surface * IMG_ReadXPMFromArray(char **xpm);
</syntaxhighlight>

== Function Parameters ==

{|
|'''xpm'''
|a null-terminated array of strings that comprise XPM data.
|}

== Return Value ==

Returns a new SDL surface, or NULL on error.

== Remarks ==

The returned surface will be an 8bpp indexed surface, if possible,
otherwise it will be 32bpp. If you always want 32-bit data, use
[[IMG_ReadXPMFromArrayToRGB888]]() instead.

When done with the returned surface, the app should dispose of it with a
call to SDL_FreeSurface().

== Version ==

This function is available since SDL_image 2.0.0.

== Related Functions ==

:[[IMG_ReadXPMFromArrayToRGB888]]

----
[[CategoryAPI]]


