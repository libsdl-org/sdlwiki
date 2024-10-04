###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SignalCondition

Restart one of the threads that are waiting on the condition variable.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_SignalCondition(SDL_Condition *cond);
```

## Function Parameters

|                                  |          |                                   |
| -------------------------------- | -------- | --------------------------------- |
| [SDL_Condition](SDL_Condition) * | **cond** | the condition variable to signal. |

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

