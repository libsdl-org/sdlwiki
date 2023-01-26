====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetDefaultAssertionHandler =

Get the default assertion handler.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_AssertionHandler SDL_GetDefaultAssertionHandler(void);
</syntaxhighlight>

== Return Value ==

Returns the default [[SDL_AssertionHandler]] that is called when an assert
triggers.

== Remarks ==

This returns the function pointer that is called by default when an
assertion is triggered. This is an internal function provided by SDL, that
is used for assertions when [[SDL_SetAssertionHandler]]() hasn't been used
to provide a different function.

== Version ==

This function is available since SDL 2.0.2.

== Related Functions ==

:[[SDL_GetAssertionHandler]]

----
[[CategoryAPI]]


