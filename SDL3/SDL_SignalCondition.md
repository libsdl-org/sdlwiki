###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SignalCondition

Restart one of the threads that are waiting on the condition variable.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
int SDL_SignalCondition(SDL_Condition *cond);
```

## Function Parameters

|              |                                  |
| ------------ | -------------------------------- |
| **cond**     | the condition variable to signal |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_BroadcastCondition](SDL_BroadcastCondition)
- [SDL_WaitCondition](SDL_WaitCondition)
- [SDL_WaitConditionTimeout](SDL_WaitConditionTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

