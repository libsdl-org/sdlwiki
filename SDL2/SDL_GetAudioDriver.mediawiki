====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetAudioDriver =

Use this function to get the name of a built in audio driver.

== Syntax ==

<syntaxhighlight lang='c'>
const char* SDL_GetAudioDriver(int index);
</syntaxhighlight>

== Function Parameters ==

{|
|'''index'''
|the index of the audio driver; the value ranges from 0 to [[SDL_GetNumAudioDrivers]]() - 1
|}

== Return Value ==

Returns the name of the audio driver at the requested index, or NULL if an
invalid index was specified.

== Remarks ==

The list of audio drivers is given in the order that they are normally
initialized by default; the drivers that seem more reasonable to choose
first (as far as the SDL developers believe) are earlier in the list.

The names of drivers are all simple, low-ASCII identifiers, like "alsa",
"coreaudio" or "xaudio2". These never have Unicode characters, and are not
meant to be proper names.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_GetNumAudioDrivers]]

----
[[CategoryAPI]]


