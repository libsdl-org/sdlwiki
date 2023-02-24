====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_GroupCount =

Returns the number of channels in a group.

== Syntax ==

<syntaxhighlight lang='c'>
int Mix_GroupCount(int tag);
</syntaxhighlight>

== Function Parameters ==

{|
|'''tag'''
|an arbitrary value, assigned to channels, to search for.
|}

== Return Value ==

Returns the number of channels assigned the specified tag.

== Remarks ==

If tag is -1, this will return the total number of channels allocated,
regardless of what their tag might be.

== Version ==

This function is available since SDL_mixer 2.0.0.

----
[[CategoryAPI]]


