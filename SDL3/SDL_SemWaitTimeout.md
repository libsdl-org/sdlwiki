###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SemWaitTimeout

Wait until a semaphore has a positive value and then decrements it.

## Syntax

```c
int SDL_SemWaitTimeout(SDL_sem *sem, Sint32 timeoutMS);

```

## Function Parameters

|                   |                                            |
| ----------------- | ------------------------------------------ |
| **sem**           | the semaphore to wait on                   |
| **timeoutMS**     | the length of the timeout, in milliseconds |

## Return Value

Returns 0 if the wait succeeds, `[SDL_MUTEX_TIMEDOUT](SDL_MUTEX_TIMEDOUT)`
if the wait does not succeed in the allotted time, or a negative error code
on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function suspends the calling thread until either the semaphore
pointed to by `sem` has a positive value, the call is interrupted by a
signal or error, or the specified time has elapsed. If the call is
successful it will atomically decrement the semaphore value.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
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
    const Uint32 timeout = 1000; /* wake up every second */

    while (!SDL_AtomicGet(&done)) {
        if (SDL_SemWaitTimeout(sem, timeout) == 0 && data_available()) {
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
```

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore)
* [SDL_DestroySemaphore](SDL_DestroySemaphore)
* [SDL_SemPost](SDL_SemPost)
* [SDL_SemTryWait](SDL_SemTryWait)
* [SDL_SemValue](SDL_SemValue)
* [SDL_SemWait](SDL_SemWait)

----
[CategoryAPI](CategoryAPI), [CategoryMutex](CategoryMutex)


