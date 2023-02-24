====== (This function is part of SDL_mixer, a separate library from SDL.) ======
= Mix_GetTimidityCfg =

Get full path of a previously-specified Timidity config file.

== Syntax ==

<syntaxhighlight lang='c'>
const char* Mix_GetTimidityCfg(void);
</syntaxhighlight>

== Return Value ==

Returns the previously-specified path, or NULL if not set.

== Remarks ==

For example, "/etc/timidity.cfg"

If a path has never been specified, this returns NULL.

This returns a pointer to internal memory, and it should not be modified or
free'd by the caller.

== Version ==

This function is available since SDL_mixer 2.6.0.

== Related Functions ==

:[[Mix_SetTimidityCfg]]

----
[[CategoryAPI]]


