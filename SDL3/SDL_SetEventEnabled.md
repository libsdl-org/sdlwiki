###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetEventEnabled

Set the state of processing events by type.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
void SDL_SetEventEnabled(Uint32 type, SDL_bool enabled);
```

## Function Parameters

|                      |             |                                                                    |
| -------------------- | ----------- | ------------------------------------------------------------------ |
| Uint32               | **type**    | the type of event; see [SDL_EventType](SDL_EventType) for details. |
| [SDL_bool](SDL_bool) | **enabled** | whether to process the event or not.                               |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_EventEnabled](SDL_EventEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

