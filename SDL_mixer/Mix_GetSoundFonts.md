====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_GetSoundFonts =

Get SoundFonts paths to use by supported MIDI backends.

== Syntax ==

<syntaxhighlight lang='c'>
const char* Mix_GetSoundFonts(void);
</syntaxhighlight>

== Return Value ==

Returns semicolon-separated list of sound font paths.

== Remarks ==

There are several factors that determine what will be reported by this
function:

* If the boolean _SDL hint_ <code>"SDL_FORCE_SOUNDFONTS"</code> is set, AND the <code>"SDL_SOUNDFONTS"</code> _environment variable_ is also set, this function will return that environment variable regardless of whether [[Mix_SetSoundFounts]]() was ever called.
* Otherwise, if [[Mix_SetSoundFonts]]() was successfully called with a non-NULL path, this function will return the string passed to that function.
* Otherwise, if the <code>"SDL_SOUNDFONTS"</code> variable is set, this function will return that environment variable.
* Otherwise, this function will search some common locations on the filesystem, and if it finds a SoundFont there, it will return that.
* Failing everything else, this function returns NULL.

This returns a pointer to internal (possibly read-only) memory, and it
should not be modified or free'd by the caller.

== Version ==

This function is available since SDL_mixer 2.0.0.

----
[[CategoryAPI]]


