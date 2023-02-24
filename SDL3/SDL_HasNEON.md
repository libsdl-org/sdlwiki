====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
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

This function is available since SDL 3.0.0.

----
[[CategoryAPI]]


