====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_FadeInMusic =

Play a new music object, fading in the audio.

== Syntax ==

<syntaxhighlight lang='c'>
int Mix_FadeInMusic(Mix_Music *music, int loops, int ms);
</syntaxhighlight>

== Function Parameters ==

{|
|'''music'''
|the new music object to play.
|-
|'''loop'''
|the number of times the chunk should loop, -1 to loop (not actually) infinitely.
|-
|'''ms'''
|the number of milliseconds to spend fading in.
|}

== Return Value ==

Returns zero on success, -1 on error.

== Remarks ==

This will start the new music playing, much like [[Mix_PlayMusic]]() will,
but will start the music playing at silence and fade in to its normal
volume over the specified number of milliseconds.

If there is already music playing, that music will be halted and the new
music object will take its place.

If <code>loops</code> is greater than zero, loop the music that many times.
If <code>loops</code> is -1, loop "infinitely" (~65000 times).

Fading music will change it's volume progressively, as if
[[Mix_VolumeMusic]]() was called on it (which is to say: you probably
shouldn't call [[Mix_VolumeMusic]]() on fading music).

== Version ==

This function is available since SDL_mixer 2.0.0.

----
[[CategoryAPI]]


