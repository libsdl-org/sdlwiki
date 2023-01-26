====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_HasAVX =

Determine whether the CPU has AVX features.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_bool SDL_HasAVX(void);
</syntaxhighlight>

== Return Value ==

Returns [[SDL_TRUE]] if the CPU has AVX features or [[SDL_FALSE]] if not.

== Remarks ==

This always returns false on CPUs that aren't using Intel instruction sets.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_HasAltiVec]]
:[[SDL_HasAVX2]]
:[[SDL_HasMMX]]
:[[SDL_HasRDTSC]]
:[[SDL_HasSSE]]
:[[SDL_HasSSE2]]
:[[SDL_HasSSE3]]
:[[SDL_HasSSE41]]
:[[SDL_HasSSE42]]

----
[[CategoryAPI]], [[CategoryCPU]]
<!-- #See the Style Guide for instructions on editing the footer. -->


