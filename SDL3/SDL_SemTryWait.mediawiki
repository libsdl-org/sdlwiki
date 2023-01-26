====== (This is the documentation for SDL3, which is under heavy development and the API is changing! [https://wiki.libsdl.org/SDL2/ SDL2] is the current stable version!) ======
= SDL_SemTryWait =

See if a semaphore has a positive value and decrement it if it does.

== Syntax ==

<syntaxhighlight lang='c'>
int SDL_SemTryWait(SDL_sem *sem);
</syntaxhighlight>

== Function Parameters ==

{|
|'''sem'''
|the semaphore to wait on
|}

== Return Value ==

Returns 0 if the wait succeeds, <code>[[SDL_MUTEX_TIMEDOUT]]</code> if the
wait would block, or a negative error code on failure; call
[[SDL_GetError]]() for more information.

== Remarks ==

This function checks to see if the semaphore pointed to by <code>sem</code>
has a positive value and atomically decrements the semaphore value if it
does. If the semaphore doesn't have a positive value, the function
immediately returns [[SDL_MUTEX_TIMEDOUT]].

== Version ==

This function is available since SDL 3.0.0.

== Code Examples ==

<syntaxhighlight lang='c++'>
SDL_atomic_t done;
SDL_sem *sem;

SDL_AtomicSet(&done, 0);
sem = SDL_CreateSemaphore(0);
.
.
Thread A:
    while (!SDL_AtomicGet(&done)) {
        add_data_to_queue();
        SDL_SemPost(sem);
    }

Thread B:
    while (!SDL_AtomicGet(&done)) {
        if (SDL_SemTryWait(sem) == 0 && data_available()) {
            get_data_from_queue();
        }
        ... do other processing
    }
.
.
SDL_AtomicSet(&done, 1);
SDL_SemPost(sem);
wait_for_threads();
SDL_DestroySemaphore(sem);
</syntaxhighlight>

== Related Functions ==

:[[SDL_CreateSemaphore]]
:[[SDL_DestroySemaphore]]
:[[SDL_SemPost]]
:[[SDL_SemValue]]
:[[SDL_SemWait]]
:[[SDL_SemWaitTimeout]]

----
[[CategoryAPI]], [[CategoryMutex]]


