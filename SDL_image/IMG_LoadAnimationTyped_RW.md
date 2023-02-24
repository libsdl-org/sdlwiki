====== (This function is part of SDL_image, a separate library from SDL.) ======
= IMG_LoadAnimationTyped_RW =

Load an animation from an SDL datasource 

== Syntax ==

<syntaxhighlight lang='c'>
IMG_Animation * IMG_LoadAnimationTyped_RW(SDL_RWops *src, int freesrc, const char *type);
</syntaxhighlight>

== Function Parameters ==

{|
|'''src'''
|an SDL_RWops that data will be read from.
|-
|'''freesrc'''
|non-zero to close/free the SDL_RWops before returning, zero to leave it open.
|-
|'''type'''
|a filename extension that represent this data ("GIF", etc).
|}

== Return Value ==

Returns a new [[IMG_Animation]], or NULL on error.

== Remarks ==

Even though this function accepts a file type, SDL_image may still try
other decoders that are capable of detecting file type from the contents of
the image data, but may rely on the caller-provided type string for formats
that it cannot autodetect. If <code>type</code> is NULL, SDL_image will
rely solely on its ability to guess the format.

If <code>freesrc</code> is non-zero, the RWops will be closed before
returning, whether this function succeeds or not. SDL_image reads
everything it needs from the RWops during this call in any case.

When done with the returned animation, the app should dispose of it with a
call to [[IMG_FreeAnimation]]().

== Version ==

This function is available since SDL_image 2.6.0.

== Related Functions ==

:[[IMG_LoadAnimation]]
:[[IMG_LoadAnimation_RW]]
:[[IMG_FreeAnimation]]

----
[[CategoryAPI]]


