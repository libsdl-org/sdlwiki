###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasEvents

Check for the existence of certain event types in the event queue.

## Syntax

```c
SDL_bool SDL_HasEvents(Uint32 minType, Uint32 maxType);

```

## Function Parameters

|                 |                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------- |
| **minType**     | the low end of event type to be queried, inclusive; see [SDL_EventType](SDL_EventType.md) for details  |
| **maxType**     | the high end of event type to be queried, inclusive; see [SDL_EventType](SDL_EventType.md) for details |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if events with type >= `minType` and <=
`maxType` are present, or [SDL_FALSE](SDL_FALSE.md) if not.

## Remarks

If you need to check for a single event type, use
[SDL_HasEvent](SDL_HasEvent.md)() instead.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HasEvents](SDL_HasEvents.md)

----
[CategoryAPI](CategoryAPI.md)
