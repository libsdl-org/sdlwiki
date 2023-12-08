###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FlushEvents

Clear events of a range of types from the event queue.

## Syntax

```c
void SDL_FlushEvents(Uint32 minType, Uint32 maxType);

```

## Function Parameters

|                 |                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------- |
| **minType**     | the low end of event type to be cleared, inclusive; see [SDL_EventType](SDL_EventType.md) for details  |
| **maxType**     | the high end of event type to be cleared, inclusive; see [SDL_EventType](SDL_EventType.md) for details |

## Remarks

This will unconditionally remove any events from the queue that are in the
range of `minType` to `maxType`, inclusive. If you need to remove a single
event type, use [SDL_FlushEvent](SDL_FlushEvent.md)() instead.

It's also normal to just ignore events you don't care about in your event
loop without calling this function.

This function only affects currently queued events. If you want to make
sure that all pending OS events are flushed, you can call
[SDL_PumpEvents](SDL_PumpEvents.md)() on the main thread immediately before
the flush call.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_FlushEvent](SDL_FlushEvent.md)

----
[CategoryAPI](CategoryAPI.md)
