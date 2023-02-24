###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetEventEnabled

Set the state of processing events by type.

## Syntax

```c
void SDL_SetEventEnabled(Uint32 type, SDL_bool enabled);

```

## Function Parameters

|                 |                                                                   |
| --------------- | ----------------------------------------------------------------- |
| **type**        | the type of event; see [SDL_EventType](SDL_EventType) for details |
| **enabled**     | whether to process the event or not                               |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_IsEventEnabled](SDL_IsEventEnabled)

----
[CategoryAPI](CategoryAPI)

