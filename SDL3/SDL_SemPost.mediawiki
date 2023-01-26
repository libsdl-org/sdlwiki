====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_SemPost =

Atomically increment a semaphore's value and wake waiting threads.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SemPost(SDL_sem *sem);
</syntaxhighlight>

== Function Parameters ==

{|
|'''sem'''
|the semaphore to increment
|}

== Return Value ==

Returns 0 on success or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Version ==

This function is available since SDL 3.0.0.

== Code Examples ==

<<Include(SDL_CreateSemaphore, , , from="## Begin Semaphore Example", to="## End Semaphore Example")>>

== Related Functions ==

:[[SDL_CreateSemaphore]]
:[[SDL_DestroySemaphore]]
:[[SDL_SemTryWait]]
:[[SDL_SemValue]]
:[[SDL_SemWait]]
:[[SDL_SemWaitTimeout]]

----
[[CategoryAPI]], [[CategoryMutex]]


