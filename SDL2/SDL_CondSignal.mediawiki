====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_CondSignal =

Restart one of the threads that are waiting on the condition variable.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_CondSignal(SDL_cond * cond);
</syntaxhighlight>

== Function Parameters ==

{|
|'''cond'''
|the condition variable to signal
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CondBroadcast]]
:[[SDL_CondWait]]
:[[SDL_CondWaitTimeout]]
:[[SDL_CreateCond]]
:[[SDL_DestroyCond]]

----
[[CategoryAPI]]


