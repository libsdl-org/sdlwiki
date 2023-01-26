====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_InitSubSystem =

Compatibility function to initialize the SDL library.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_InitSubSystem(Uint32 flags);
</syntaxhighlight>

== Function Parameters ==

{|
|'''flags'''
|any of the flags used by [[SDL_Init]](); see [[SDL_Init]] for details.
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

In SDL2, this function and [[SDL_Init]]() are interchangeable.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_Init]]
:[[SDL_Quit]]
:[[SDL_QuitSubSystem]]

----
[[CategoryAPI]]


