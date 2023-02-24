====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_AndroidGetExternalStorageState =

Get the current state of external storage.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_AndroidGetExternalStorageState(void);
</syntaxhighlight>

== Return Value ==

Returns the current state of external storage on success or 0 on failure;
call [[SDL_GetError]]() for more information.

== Remarks ==

The current state of external storage, a bitmask of these values:
<code>[[SDL_ANDROID_EXTERNAL_STORAGE_READ]]</code>,
<code>[[SDL_ANDROID_EXTERNAL_STORAGE_WRITE]]</code>.

If external storage is currently unavailable, this will return 0.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_AndroidGetExternalStoragePath]]

----
[[CategoryAPI]]


