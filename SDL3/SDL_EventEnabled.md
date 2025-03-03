# SDL_EventEnabled

Query the state of processing events by type.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
bool SDL_EventEnabled(Uint32 type);
```

## Function Parameters

|                  |          |                                                                    |
| ---------------- | -------- | ------------------------------------------------------------------ |
| [Uint32](Uint32) | **type** | the type of event; see [SDL_EventType](SDL_EventType) for details. |

## Return Value

(bool) Returns true if the event is being processed, false otherwise.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetEventEnabled](SDL_SetEventEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

