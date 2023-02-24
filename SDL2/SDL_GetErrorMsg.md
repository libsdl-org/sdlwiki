====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetErrorMsg =

Get the last error message that was set for the current thread.

== Syntax ==

<syntaxhighlight lang='c'>
char * SDL_GetErrorMsg(char *errstr, int maxlen);
</syntaxhighlight>

== Function Parameters ==

{|
|'''errstr'''
|A buffer to fill with the last error message that was set for the current thread
|-
|'''maxlen'''
|The size of the buffer pointed to by the errstr parameter
|}

== Return Value ==

Returns the pointer passed in as the <code>errstr</code> parameter.

== Remarks ==

This allows the caller to copy the error string into a provided buffer, but
otherwise operates exactly the same as [[SDL_GetError]]().

== Version ==

This function is available since SDL 2.0.14.

== Related Functions ==

:[[SDL_GetError]]

----
[[CategoryAPI]]


