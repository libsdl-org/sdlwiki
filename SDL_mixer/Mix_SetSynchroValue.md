====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_SetSynchroValue =

This function does nothing, do not use.

== Syntax ==

<syntaxhighlight lang='c'>
int Mix_SetSynchroValue(int value);
</syntaxhighlight>

== Function Parameters ==

{|
|'''value'''
|this parameter is ignored.
|}

== Return Value ==

Returns -1.

== Remarks ==

This was probably meant to expose a feature, but no codecs support it, so
it only remains for binary compatibility.

Calling this function is a legal no-op that returns -1.

== Version ==

This function is available since SDL_mixer 2.0.0.

----
[[CategoryAPI]]


