====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_TryLockMutex =

Try to lock a mutex without blocking.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_TryLockMutex(SDL_mutex * mutex) SDL_TRY_ACQUIRE(0, mutex);
</syntaxhighlight>

== Function Parameters ==

{|
|'''mutex'''
|the mutex to try to lock
|}

== Return Value ==

Returns 0, <code>[[SDL_MUTEX_TIMEDOUT]]</code>, or -1 on error; call
[[SDL_GetError]]() for more information.

== Remarks ==

This works just like [[SDL_LockMutex]](), but if the mutex is not
available, this function returns <code>[[SDL_MUTEX_TIMEOUT]]</code>
immediately.

This technique is useful if you need exclusive access to a resource but
don't want to wait for it, and will return to it to try again later.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_CreateMutex]]
:[[SDL_DestroyMutex]]
:[[SDL_LockMutex]]
:[[SDL_UnlockMutex]]

----
[[CategoryAPI]]


