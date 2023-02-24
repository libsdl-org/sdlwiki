====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_GetCPUCount =

Get the number of CPU cores available.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_GetCPUCount(void);
</syntaxhighlight>

== Return Value ==

Returns the total number of logical CPU cores. On CPUs that include
technologies such as hyperthreading, the number of logical cores may be
more than the number of physical cores.

== Version ==

This function is available since SDL 2.0.0.

----
[[CategoryAPI]]


