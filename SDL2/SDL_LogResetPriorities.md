====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_LogResetPriorities =

Reset all priorities to default.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_LogResetPriorities(void);
</syntaxhighlight>

== Remarks ==

This is called by [[SDL_Quit]]().

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_LogSetAllPriority]]
:[[SDL_LogSetPriority]]

----
[[CategoryAPI]]


