====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_GetMusicHookData =

Get a pointer to the user data for the current music hook.

== Syntax ==

<syntaxhighlight lang='c'>
void * Mix_GetMusicHookData(void);
</syntaxhighlight>

== Return Value ==

Returns pointer to the user data previously passed to [[Mix_HookMusic]].

== Remarks ==

This returns the <code>arg</code> pointer last passed to
[[Mix_HookMusic]](), or NULL if that function has never been called.

== Version ==

This function is available since SDL_mixer 2.0.0.

----
[[CategoryAPI]]


