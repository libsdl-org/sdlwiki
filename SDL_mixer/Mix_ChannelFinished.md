====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_ChannelFinished =

Set a callback that runs when a channel has finished playing.

== Syntax ==

<syntaxhighlight lang='c'>
void Mix_ChannelFinished(void (SDLCALL *channel_finished)(int channel));
</syntaxhighlight>

== Function Parameters ==

{|
|'''channel_finished'''
|the callback function to become the new notification mechanism.
|}

== Remarks ==

The callback may be called from the mixer's audio callback or it could be
called as a result of [[Mix_HaltChannel]](), etc.

The callback has a single parameter, <code>channel</code>, which says what
mixer channel has just stopped.

Do not call SDL_LockAudio() from this callback; you will either be inside
the audio callback, or SDL_mixer will explicitly lock the audio before
calling your callback.

A NULL pointer will disable the callback.

== Version ==

This function is available since SDL_mixer 2.0.0.

----
[[CategoryAPI]]


