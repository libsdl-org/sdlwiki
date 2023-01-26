====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_MixAudio =

This function is a legacy means of mixing audio.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_MixAudio(Uint8 * dst, const Uint8 * src,
                  Uint32 len, int volume);
</syntaxhighlight>

== Function Parameters ==

{|
|'''dst'''
|the destination for the mixed audio
|-
|'''src'''
|the source audio buffer to be mixed
|-
|'''len'''
|the length of the audio buffer in bytes
|-
|'''volume'''
|ranges from 0 - 128, and should be set to [[SDL_MIX_MAXVOLUME]] for full audio volume
|}

== Remarks ==

This function is equivalent to calling...

<syntaxhighlight lang='c'>
SDL_MixAudioFormat(dst, src, format, len, volume);
</syntaxhighlight>

...where <code>format</code> is the obtained format of the audio device
from the legacy [[SDL_OpenAudio]]() function.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_MixAudioFormat]]

----
[[CategoryAPI]]


