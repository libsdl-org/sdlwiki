###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitCondition

Wait until a condition variable is signaled.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
int SDL_WaitCondition(SDL_Condition *cond, SDL_Mutex *mutex);

```

## Function Parameters

|               |                                            |
| ------------- | ------------------------------------------ |
| **cond**      | the condition variable to wait on          |
| **mutex**     | the mutex used to coordinate thread access |

## Return Value

Returns 0 when it is signaled or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This function unlocks the specified `mutex` and waits for another thread to
call [SDL_SignalCondition](SDL_SignalCondition)() or
[SDL_BroadcastCondition](SDL_BroadcastCondition)() on the condition
variable `cond`. Once the condition variable is signaled, the mutex is
re-locked and the function returns.

The mutex must be locked before calling this function. Locking the mutex
recursively (more than once) is not supported and leads to undefined
behavior.

This function is the equivalent of calling
[SDL_WaitConditionTimeout](SDL_WaitConditionTimeout)() with a time length
of -1.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_BroadcastCondition](SDL_BroadcastCondition)
- [SDL_SignalCondition](SDL_SignalCondition)
- [SDL_WaitConditionTimeout](SDL_WaitConditionTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

