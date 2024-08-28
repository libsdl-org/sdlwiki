###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitSemaphore

Wait until a semaphore has a positive value and then decrements it.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_WaitSemaphore(SDL_Semaphore *sem);
```

## Function Parameters

|                                  |         |                        |
| -------------------------------- | ------- | ---------------------- |
| [SDL_Semaphore](SDL_Semaphore) * | **sem** | the semaphore wait on. |

## Remarks

This function suspends the calling thread until the semaphore pointed to by
`sem` has a positive value, and then atomically decrement the semaphore
value.

This function is the equivalent of calling
[SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)() with a time length
of -1.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c
void create_and_wait_threads(void);

#define NB_WAITER 10
SDL_Semaphore *sem;
// Increments the semaphore every 2s
int poster_thread() {
  for (int i = 0; i < NB_WAITER; i++) {
    SDL_SignalSemaphore(sem);
    SDL_Delay(2 * 1000);
  }
  return 0;
}
int waiter_thread()
{
  SDL_WaitSemaphore(sem);
  SDL_Log("Semaphore was decremented.\n");
  return 0;
}
int main() {
  sem = SDL_CreateSemaphore(0);
  create_and_wait_threads(); // 1 poster, 10 waiters
  SDL_DestroySemaphore(sem);
}

```

## See Also

- [SDL_SignalSemaphore](SDL_SignalSemaphore)
- [SDL_TryWaitSemaphore](SDL_TryWaitSemaphore)
- [SDL_WaitSemaphoreTimeout](SDL_WaitSemaphoreTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

