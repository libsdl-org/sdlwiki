====== (This function is part of SDL_image, a separate library from SDL.) ======
= IMG_LoadSizedSVG_RW =

Load an SVG image, scaled to a specific size.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_Surface * IMG_LoadSizedSVG_RW(SDL_RWops *src, int width, int height);
</syntaxhighlight>

== Function Parameters ==

{|
|'''src'''
|an SDL_RWops to load SVG data from.
|-
|'''width'''
|desired width of the generated surface, in pixels.
|-
|'''height'''
|desired height of the generated surface, in pixels.
|}

== Return Value ==

Returns a new SDL surface, or NULL on error.

== Remarks ==

Since SVG files are resolution-independent, you specify the size you would
like the output image to be and it will be generated at those dimensions.

Either width or height may be 0 and the image will be auto-sized to
preserve aspect ratio.

When done with the returned surface, the app should dispose of it with a
call to SDL_FreeSurface().

== Version ==

This function is available since SDL_image 2.6.0.

----
[[CategoryAPI]]


