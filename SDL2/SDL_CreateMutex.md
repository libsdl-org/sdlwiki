====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_CreateMutex =

Create a new mutex.

== Syntax ==

<syntaxhighlight lang='c'>
SDL_mutex* SDL_CreateMutex(void);
</syntaxhighlight>

== Return Value ==

Returns the initialized and unlocked mutex or NULL on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

All newly-created mutexes begin in the _unlocked_ state.

Calls to [[SDL_LockMutex]]() will not return while the mutex is locked by
another thread. See [[SDL_TryLockMutex]]() to attempt to lock without
blocking.

SDL mutexes are reentrant.

== Version ==

This function is available since SDL 2.0.0.

== Related Functions ==

:[[SDL_DestroyMutex]]
:[[SDL_LockMutex]]
:[[SDL_TryLockMutex]]
:[[SDL_UnlockMutex]]

----
[[CategoryAPI]]


