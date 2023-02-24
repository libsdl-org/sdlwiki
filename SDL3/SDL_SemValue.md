====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_SemValue =

Get the current value of a semaphore.

== Syntax ==

<syntaxhighlight lang='c'>
Uint32 SDL_SemValue(SDL_sem *sem);
</syntaxhighlight>

== Function Parameters ==

{|
|'''sem'''
|the semaphore to query
|}

== Return Value ==

Returns the current value of the semaphore.

== Version ==

This function is available since SDL 3.0.0.

== Related Functions ==

:[[SDL_CreateSemaphore]]

----
[[CategoryAPI]], [[CategoryMutex]]


