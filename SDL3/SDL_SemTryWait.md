###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SemTryWait

See if a semaphore has a positive value and decrement it if it does.

## Syntax

```c
int SDL_SemTryWait(SDL_sem *sem);

```

## Function Parameters

|             |                          |
| ----------- | ------------------------ |
| **sem**     | the semaphore to wait on |

## Return Value

Returns 0 if the wait succeeds, [`SDL_MUTEX_TIMEDOUT`](SDL_MUTEX_TIMEDOUT)
if the wait would block, or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function checks to see if the semaphore pointed to by `sem` has a
positive value and atomically decrements the semaphore value if it does. If
the semaphore doesn't have a positive value, the function immediately
returns [SDL_MUTEX_TIMEDOUT](SDL_MUTEX_TIMEDOUT).

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
```

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore)
* [SDL_DestroySemaphore](SDL_DestroySemaphore)
* [SDL_SemPost](SDL_SemPost)
* [SDL_SemValue](SDL_SemValue)
* [SDL_SemWait](SDL_SemWait)
* [SDL_SemWaitTimeout](SDL_SemWaitTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryMutex](CategoryMutex)


