###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BroadcastCondition

Restart all threads that are waiting on the condition variable.

## Syntax

```c
int SDL_BroadcastCondition(SDL_Condition *cond);

```

## Function Parameters

|              |                                  |
| ------------ | -------------------------------- |
| **cond**     | the condition variable to signal |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_SignalCondition](SDL_SignalCondition)
* [SDL_WaitCondition](SDL_WaitCondition)
* [SDL_WaitConditionTimeout](SDL_WaitConditionTimeout)
* [SDL_CreateCondition](SDL_CreateCondition)
* [SDL_DestroyCondition](SDL_DestroyCondition)

----
[CategoryAPI](CategoryAPI)

