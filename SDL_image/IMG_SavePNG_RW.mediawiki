====== (This function is part of SDL_image, a separate library from SDL.) ======
= IMG_SavePNG_RW =

Save an SDL_Surface into PNG image data, via an SDL_RWops.

== Syntax ==

<syntaxhighlight lang='c'>
int IMG_SavePNG_RW(SDL_Surface *surface, SDL_RWops *dst, int freedst);
</syntaxhighlight>

== Function Parameters ==

{|
|'''surface'''
|the SDL surface to save
|-
|'''dst'''
|the SDL_RWops to save the image data to.
|}

== Return Value ==

Returns 0 if successful, -1 on error.

== Remarks ==

If you just want to save to a filename, you can use [[IMG_SavePNG]]()
instead.

== Version ==

This function is available since SDL_image 2.0.0.

== Related Functions ==

:[[IMG_SavePNG]]
:[[IMG_SaveJPG]]
:[[IMG_SaveJPG_RW]]

----
[[CategoryAPI]]


