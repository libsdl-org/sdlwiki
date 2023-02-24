====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetAudioDeviceStatus =

Use this function to get the current audio state of an audio device.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_AudioStatus SDL_GetAudioDeviceStatus(SDL_AudioDeviceID dev);
</syntaxhighlight>

== Function Parameters ==

{|
|'''dev'''
|the ID of an audio device previously opened with [[SDL_OpenAudioDevice]]()
|}

== Return Value ==

Returns the [[SDL_AudioStatus]] of the specified audio device.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_PauseAudioDevice]]

----
[[CategoryAPI]]


