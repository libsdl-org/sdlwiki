###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SemWait

Wait until a semaphore has a positive value and then decrements it.

## Syntax

```c
int SDL_SemWait(SDL_sem *sem);

```

## Function Parameters

|             |                       |
| ----------- | --------------------- |
| **sem**     | the semaphore wait on |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function suspends the calling thread until either the semaphore
pointed to by `sem` has a positive value or the call is interrupted by a
signal or error. If the call is successful it will atomically decrement the
semaphore value.

This function is the equivalent of calling
[SDL_SemWaitTimeout](SDL_SemWaitTimeout)() with a time length of
`[SDL_MUTEX_MAXWAIT](SDL_MUTEX_MAXWAIT)`.

## Version

This function is available since SDL 3.0.0.

## Code Examples

<!-- # Begin Semaphore Example -->
```c
#define NB_WAITER 10

SDL_sem *sem;

// Increments the semaphore every 2s
int poster_thread() {
  for (int i = 0; i < NB_WAITER; i++) {
    SDL_SemPost(sem);
    SDL_Delay(2 * 1000);
  }
  return 0;
}

int waiter_thread() {
  int status;

  status = SDL_SemWait(sem);
  
  if (status == 0) {
    SDL_Log("Semaphore was decremented.\n");
  } else {
    SDL_LogError(SDL_LOG_CATEGORY_APPLICATION, "An error has occured while waiting: %s\n", SDL_GetError());
  }
  return 0;
}

int main() {
  sem = SDL_CreateSemaphore(0);
  create_and_wait_threads(); // 1 poster, 10 waiters
  SDL_DestroySemaphore(sem);
}
```
<!-- # End Semaphore Example -->

## Related Functions

* [SDL_CreateSemaphore](SDL_CreateSemaphore)
* [SDL_DestroySemaphore](SDL_DestroySemaphore)
* [SDL_SemPost](SDL_SemPost)
* [SDL_SemTryWait](SDL_SemTryWait)
* [SDL_SemValue](SDL_SemValue)
* [SDL_SemWait](SDL_SemWait)
* [SDL_SemWaitTimeout](SDL_SemWaitTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryMutex](CategoryMutex)


