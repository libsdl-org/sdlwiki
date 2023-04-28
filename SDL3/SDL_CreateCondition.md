###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateCondition

Create a condition variable.

## Syntax

```c
SDL_Condition* SDL_CreateCondition(void);

```

## Return Value

Returns a new condition variable or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_BroadcastCondition](SDL_BroadcastCondition)
* [SDL_SignalCondition](SDL_SignalCondition)
* [SDL_WaitCondition](SDL_WaitCondition)
* [SDL_WaitConditionTimeout](SDL_WaitConditionTimeout)
* [SDL_DestroyCondition](SDL_DestroyCondition)

----
[CategoryAPI](CategoryAPI)

