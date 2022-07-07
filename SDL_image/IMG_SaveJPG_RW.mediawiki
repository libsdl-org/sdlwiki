====== (This function is part of SDL_image, a separate library from SDL.) ======
= IMG_SaveJPG_RW =

Save an SDL_Surface into JPEG image data, via an SDL_RWops.

== Syntax ==

<syntaxhighlight lang='c'>
int IMG_SaveJPG_RW(SDL_Surface *surface, SDL_RWops *dst, int freedst, int quality);
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

If you just want to save to a filename, you can use [[IMG_SaveJPG]]()
instead.

== Version ==

This function is available since SDL_image 2.0.2.

== Related Functions ==

:[[IMG_SaveJPG]]
:[[IMG_SavePNG]]
:[[IMG_SavePNG_RW]]

----
[[CategoryAPI]]


