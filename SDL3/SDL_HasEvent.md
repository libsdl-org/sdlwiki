# SDL_HasEvent

Check for the existence of a certain event type in the event queue.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
bool SDL_HasEvent(Uint32 type);
```

## Function Parameters

|                  |          |                                                                                  |
| ---------------- | -------- | -------------------------------------------------------------------------------- |
| [Uint32](Uint32) | **type** | the type of event to be queried; see [SDL_EventType](SDL_EventType) for details. |

## Return Value

(bool) Returns true if events matching `type` are present, or false if
events matching `type` are not present.

## Remarks

If you need to check for a range of event types, use
[SDL_HasEvents](SDL_HasEvents)() instead.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_HasEvents](SDL_HasEvents)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

