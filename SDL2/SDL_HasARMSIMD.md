====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_HasARMSIMD =

Determine whether the CPU has ARM SIMD (ARMv6) features.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_HasARMSIMD(void);
</syntaxhighlight>

== Return Value ==

Returns [[SDL_TRUE]] if the CPU has ARM SIMD features or [[SDL_FALSE]] if
not.

== Remarks ==

This is different from ARM NEON, which is a different instruction set.

This always returns false on CPUs that aren't using ARM instruction sets.

== Version ==

This function is available since SDL 2.0.12.

== Related Functions ==

:[[SDL_HasNEON]]

----
[[CategoryAPI]]


