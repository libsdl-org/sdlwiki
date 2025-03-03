# SDL_SetEventEnabled

Set the state of processing events by type.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
void SDL_SetEventEnabled(Uint32 type, bool enabled);
```

## Function Parameters

|                  |             |                                                                    |
| ---------------- | ----------- | ------------------------------------------------------------------ |
| [Uint32](Uint32) | **type**    | the type of event; see [SDL_EventType](SDL_EventType) for details. |
| bool             | **enabled** | whether to process the event or not.                               |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_EventEnabled](SDL_EventEnabled)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

