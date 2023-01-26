====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GUIDFromString =

Convert a GUID string into a ::[[SDL_GUID]] structure.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_GUID SDL_GUIDFromString(const char *pchGUID);
</syntaxhighlight>

== Function Parameters ==

{|
|'''pchGUID'''
|string containing an ASCII representation of a GUID
|}

== Return Value ==

Returns a ::[[SDL_GUID]] structure.

== Remarks ==

Performs no error checking. If this function is given a string containing
an invalid GUID, the function will silently succeed, but the GUID generated
will not be useful.

== Version ==

This function is available since SDL 2.24.0.

== Related Functions ==

:[[SDL_GUIDToString]]

----
[[CategoryAPI]]


