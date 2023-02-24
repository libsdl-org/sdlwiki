====== (This function is part of SDL_ttf, a separate library from SDL.) ======
= TTF_Linked_Version =

Query the version of SDL_ttf that the program is linked against.

== Syntax ==

<syntaxhighlight lang='c'>
const SDL_version * TTF_Linked_Version(void);
</syntaxhighlight>

== Return Value ==

Returns a pointer to the version information.

== Remarks ==

This function gets the version of the dynamically linked SDL_ttf library.
This is separate from the SDL_TTF_VERSION() macro, which tells you what
version of the SDL_ttf headers you compiled against.

This returns static internal data; do not free or modify it!

== Version ==

This function is available since SDL_ttf 2.0.12.

----
[[CategoryAPI]]


