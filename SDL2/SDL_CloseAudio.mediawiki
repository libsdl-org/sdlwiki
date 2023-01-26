====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_CloseAudio =

This function is a legacy means of closing the audio device.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_CloseAudio(void);
</syntaxhighlight>

== Remarks ==

This function is equivalent to calling...

<syntaxhighlight lang='c'>
SDL_CloseAudioDevice(1);
</syntaxhighlight>

...and is only useful if you used the legacy [[SDL_OpenAudio]]() function.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_OpenAudio]]

----
[[CategoryAPI]]


