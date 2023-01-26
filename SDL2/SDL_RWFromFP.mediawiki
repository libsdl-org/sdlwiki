====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_RWFromFP =

Use this function to create an [[SDL_RWops]] structure from a standard I/O file pointer (stdio.h's <code>FILE*</code>).

== Syntax ==

<syntaxhighlight lang='c'>
SDL_RWops* SDL_RWFromFP(void * fp,
                        SDL_bool autoclose);
</syntaxhighlight>

== Function Parameters ==

{|
|'''fp'''
|the <code>FILE*</code> that feeds the [[SDL_RWops]] stream
|-
|'''autoclose'''
|[[SDL_TRUE]] to close the <code>FILE*</code> when closing the [[SDL_RWops]], [[SDL_FALSE]] to leave the <code>FILE*</code> open when the RWops is closed
|}

== Return Value ==

Returns a pointer to the [[SDL_RWops]] structure that is created, or NULL
on failure; call [[SDL_GetError]]() for more information.

== Remarks ==

This function is not available on Windows, since files opened in an
application on that platform cannot be used by a dynamically linked
library.

On some platforms, the first parameter is a <code>void*</code>, on others,
it's a <code>FILE*</code>, depending on what system headers are available
to SDL. It is always intended to be the <code>FILE*</code> type from the C
runtime's stdio.h.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_RWclose]]
:[[SDL_RWFromConstMem]]
:[[SDL_RWFromFile]]
:[[SDL_RWFromMem]]
:[[SDL_RWread]]
:[[SDL_RWseek]]
:[[SDL_RWtell]]
:[[SDL_RWwrite]]

----
[[CategoryAPI]]


