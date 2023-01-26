====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_LockAudio =

This function is a legacy means of locking the audio device.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_LockAudio(void);
</syntaxhighlight>

== Remarks ==

New programs might want to use [[SDL_LockAudioDevice]]() instead. This
function is equivalent to calling...

<syntaxhighlight lang='c'>
SDL_LockAudioDevice(1);
</syntaxhighlight>

...and is only useful if you used the legacy [[SDL_OpenAudio]]() function.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_LockAudioDevice]]
:[[SDL_UnlockAudio]]
:[[SDL_UnlockAudioDevice]]

----
[[CategoryAPI]]


