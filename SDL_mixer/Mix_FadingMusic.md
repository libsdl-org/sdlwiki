====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_FadingMusic =

Query the fading status of the music stream.

== Syntax ==

<syntaxhighlight lang='c'>
Mix_Fading Mix_FadingMusic(void);
</syntaxhighlight>

== Return Value ==

Returns the current fading status of the music stream.

== Remarks ==

This reports one of three values:

* <code>[[MIX_NO_FADING]]</code>
* <code>[[MIX_FADING_OUT]]</code>
* <code>[[MIX_FADING_IN]]</code>

If music is not currently playing, this returns
<code>[[MIX_NO_FADING]]</code>.

== Version ==

This function is available since SDL_mixer 2.0.0.

----
[[CategoryAPI]]


