###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_EventEnabled

Query the state of processing events by type.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
bool SDL_EventEnabled(Uint32 type);
```

## Function Parameters

|        |          |                                                                    |
| ------ | -------- | ------------------------------------------------------------------ |
| Uint32 | **type** | the type of event; see [SDL_EventType](SDL_EventType) for details. |

## Return Value

(bool) Returns true if the event is being processed, false otherwise.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SetEventEnabled](SDL_SetEventEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

