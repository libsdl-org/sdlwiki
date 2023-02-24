====== (This function is part of SDL_image, a separate library from SDL.) ======
= IMG_LoadAnimation =

Load an animation from a file.

== Syntax ==

<syntaxhighlight lang='c'>
IMG_Animation * IMG_LoadAnimation(const char *file);
</syntaxhighlight>

== Function Parameters ==

{|
|'''file'''
|path on the filesystem containing an animated image.
|}

== Return Value ==

Returns a new [[IMG_Animation]], or NULL on error.

== Remarks ==

When done with the returned animation, the app should dispose of it with a
call to [[IMG_FreeAnimation]]().

== Version ==

This function is available since SDL_image 2.6.0.

== Related Functions ==

:[[IMG_FreeAnimation]]

----
[[CategoryAPI]]


