====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_FadeOutChannel =

Halt a channel after fading it out for a specified time.

== Syntax ==

<syntaxhighlight lang='c'>
int Mix_FadeOutChannel(int which, int ms);
</syntaxhighlight>

== Function Parameters ==

{|
|'''which'''
|the channel to fade out.
|-
|'''ms'''
|number of milliseconds to fade before halting the channel.
|}

== Return Value ==

Returns the number of channels scheduled to fade.

== Remarks ==

This will begin a channel fading from its current volume to silence over
<code>ms</code> milliseconds. After that time, the channel is halted.

Any halted channels will have any currently-registered effects
deregistered, and will call any callback specified by
[[Mix_ChannelFinished]]() once the halt occurs.

A fading channel will change it's volume progressively, as if
[[Mix_Volume]]() was called on it (which is to say: you probably shouldn't
call [[Mix_Volume]]() on a fading channel).

Note that this function does not block for the number of milliseconds
requested; it just schedules the chunk to fade and notes the time for the
mixer to manage later, and returns immediately.

== Version ==

This function is available since SDL_mixer 2.0.0.

----
[[CategoryAPI]]


