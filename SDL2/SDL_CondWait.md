###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CondWait

Wait until a condition variable is signaled.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mutex.h)

## Syntax

```c
int SDL_CondWait(SDL_cond * cond, SDL_mutex * mutex);
```

## Function Parameters

|                          |           |                                            |
| ------------------------ | --------- | ------------------------------------------ |
| [SDL_cond](SDL_cond) *   | **cond**  | the condition variable to wait on          |
| [SDL_mutex](SDL_mutex) * | **mutex** | the mutex used to coordinate thread access |

## Return Value

(int) Returns 0 when it is signaled or a negative error code on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function unlocks the specified `mutex` and waits for another thread to
call [SDL_CondSignal](SDL_CondSignal)() or
[SDL_CondBroadcast](SDL_CondBroadcast)() on the condition variable `cond`.
Once the condition variable is signaled, the mutex is re-locked and the
function returns.

The mutex must be locked before calling this function.

This function is the equivalent of calling
[SDL_CondWaitTimeout](SDL_CondWaitTimeout)() with a time length of
[`SDL_MUTEX_MAXWAIT`](SDL_MUTEX_MAXWAIT).

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CondBroadcast](SDL_CondBroadcast)
- [SDL_CondSignal](SDL_CondSignal)
- [SDL_CondWaitTimeout](SDL_CondWaitTimeout)
- [SDL_CreateCond](SDL_CreateCond)
- [SDL_DestroyCond](SDL_DestroyCond)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

