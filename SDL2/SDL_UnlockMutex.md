====== (This is the legacy documentation for stable SDL2, the current stable version; [https://wiki.libsdl.org/SDL3/ SDL3] is the current development version.) ======
= SDL_UnlockMutex =

Unlock the mutex.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_UnlockMutex(SDL_mutex * mutex) SDL_RELEASE(mutex);
</syntaxhighlight>

== Function Parameters ==

{|
|'''mutex'''
|the mutex to unlock.
|}

== Return Value ==

Returns 0, or -1 on error.

== Remarks ==

It is legal for the owning thread to lock an already-locked mutex. It must
unlock it the same number of times before it is actually made available for
other threads in the system (this is known as a "recursive mutex").

It is an error to unlock a mutex that has not been locked by the current
thread, and doing so results in undefined behavior.

It is also an error to unlock a mutex that isn't locked at all.

== Version ==

This function is available since SDL 2.0.0.

----
[[CategoryAPI]]


