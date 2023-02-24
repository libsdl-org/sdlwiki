====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HasNEON =

Determine whether the CPU has NEON (ARM SIMD) features.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_HasNEON(void);
</syntaxhighlight>

== Return Value ==

Returns [[SDL_TRUE]] if the CPU has ARM NEON features or [[SDL_FALSE]] if
not.

== Remarks ==

This always returns false on CPUs that aren't using ARM instruction sets.

== Version ==

This function is available since SDL 2.0.6.

----
[[CategoryAPI]]


