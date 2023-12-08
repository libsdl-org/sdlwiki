###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_DestroyCondition

Destroy a condition variable.

## Syntax

```c
void SDL_DestroyCondition(SDL_Condition *cond);

```

## Function Parameters

|              |                                   |
| ------------ | --------------------------------- |
| **cond**     | the condition variable to destroy |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_BroadcastCondition](SDL_BroadcastCondition.md)
* [SDL_SignalCondition](SDL_SignalCondition.md)
* [SDL_WaitCondition](SDL_WaitCondition.md)
* [SDL_WaitConditionTimeout](SDL_WaitConditionTimeout.md)
* [SDL_CreateCondition](SDL_CreateCondition.md)

----
[CategoryAPI](CategoryAPI.md)
