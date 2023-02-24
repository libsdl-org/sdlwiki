====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_CondWaitTimeout =

Wait until a condition variable is signaled or a certain time has passed.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_CondWaitTimeout(SDL_cond *cond,
                        SDL_mutex *mutex, Sint32 timeoutMS);
</syntaxhighlight>

== Function Parameters ==

{|
|'''cond'''
|the condition variable to wait on
|-
|'''mutex'''
|the mutex used to coordinate thread access
|-
|'''timeoutMS'''
|the maximum time to wait, in milliseconds, or <code>[[SDL_MUTEX_MAXWAIT]]</code> to wait indefinitely
|}

== Return Value ==

Returns 0 if the condition variable is signaled,
<code>[[SDL_MUTEX_TIMEDOUT]]</code> if the condition is not signaled in the
allotted time, or a negative error code on failure; call [[SDL_GetError]]()
for more information.

== Remarks ==

This function unlocks the specified <code>mutex</code> and waits for
another thread to call [[SDL_CondSignal]]() or [[SDL_CondBroadcast]]() on
the condition variable <code>cond</code>, or for the specified time to
elapse. Once the condition variable is signaled or the time elapsed, the
mutex is re-locked and the function returns.

The mutex must be locked before calling this function. Locking the mutex
recursively (more than once) is not supported and leads to undefined
behavior.

== Version ==

This function is available since SDL 3.0.0.

== Code Examples ==

<syntaxhighlight lang='c++'>
SDL_bool condition = SDL_FALSE;
SDL_mutex *lock;
SDL_cond *cond;

lock = SDL_CreateMutex();
cond = SDL_CreateCond();
.
.
Thread A:
    const Uint32 timeout = 1000; /* wake up every second */

    while (!done) {
        SDL_LockMutex(lock);
        while (!condition && SDL_CondWaitTimeout(cond, lock, timeout) == 0) {
            continue;
        }
        SDL_UnlockMutex(lock);

        if (condition) {
            ...
        }

        ... do some periodic work
    }

Thread B:
    SDL_LockMutex(lock);
    ...
    condition = SDL_TRUE;
    ...
    SDL_CondSignal(cond);
    SDL_UnlockMutex(lock);
.
.
SDL_DestroyCond(cond);
SDL_DestroyMutex(lock);
</syntaxhighlight>

== Related Functions ==

:[[SDL_CondBroadcast]]
:[[SDL_CondSignal]]
:[[SDL_CondWait]]
:[[SDL_CreateCond]]
:[[SDL_DestroyCond]]

----
[[CategoryAPI]], [[CategoryMutex]]


