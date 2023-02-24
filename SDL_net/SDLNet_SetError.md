====== (This function is part of SDL_net, a separate library from SDL.) ======
= SDLNet_SetError =

Set an error message to be retrieved with [[SDLNet_GetError]].

== Syntax ==

<syntaxhighlight lang='c'>
void SDLNet_SetError(const char *fmt, ...);
</syntaxhighlight>

== Function Parameters ==

{|
|'''fmt'''
|a printf-style format string for the error message.
|}

== Remarks ==

Generally you don't need to call this (SDL_net will use it internally to
report errors), but it could be useful if you need to inject an error
message of your own in here.

== Version ==

This function is available since SDL_net 2.0.0.

----
[[CategoryAPI]]


