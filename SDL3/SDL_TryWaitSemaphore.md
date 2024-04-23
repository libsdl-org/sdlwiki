###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TryWaitSemaphore

See if a semaphore has a positive value and decrement it if it does.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
int SDL_TryWaitSemaphore(SDL_Semaphore *sem);

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

```c
// BEWARE: This code example was migrated from the SDL2 Wiki, by only updating the names.

void add_data_to_queue(void);
void get_data_from_queue(void);
int data_available(void);
void wait_for_threads(void);

SDL_AtomicInt done;
SDL_Semaphore *sem;
SDL_AtomicSet(&done, 0);
sem = SDL_CreateSemaphore(0);

Thread_A:
    while (!SDL_AtomicGet(&done)) {
        add_data_to_queue();
        SDL_PostSemaphore(sem);
    }
Thread_B:
    while (!SDL_AtomicGet(&done)) {
        if (SDL_TryWaitSemaphore(sem) == 0 && data_available()) {
            get_data_from_queue();
        }
        /* do other processing */
    }

SDL_AtomicSet(&done, 1);
SDL_PostSemaphore(sem);
wait_for_threads();
SDL_DestroySemaphore(sem);
```

## See Also

* [SDL_PostSemaphore](SDL_PostSemaphore)
* [SDL_WaitSemaphore](SDL_WaitSemaphore)
* [SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

