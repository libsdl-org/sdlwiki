====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_DestroySemaphore =

Destroy a semaphore.

== Syntax ==

<syntaxhighlight lang='c'>
void SDL_DestroySemaphore(SDL_sem * sem);
</syntaxhighlight>

== Function Parameters ==

{|
|'''sem'''
|the semaphore to destroy
|}

== Remarks ==

It is not safe to destroy a semaphore if there are threads currently
waiting on it.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateSemaphore]]
:[[SDL_SemPost]]
:[[SDL_SemTryWait]]
:[[SDL_SemValue]]
:[[SDL_SemWait]]
:[[SDL_SemWaitTimeout]]

----
[[CategoryAPI]]


