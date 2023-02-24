====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_LogResetPriorities =

Reset all priorities to default.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_LogResetPriorities(void);
</syntaxhighlight>

== Remarks ==

This is called by [[SDL_Quit]]().

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_LogSetAllPriority]]
:[[SDL_LogSetPriority]]

----
[[CategoryAPI]], [[CategoryLog]]


