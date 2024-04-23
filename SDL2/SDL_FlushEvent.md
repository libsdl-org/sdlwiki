###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_FlushEvent

Clear events of a specific type from the event queue.

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h)

## Syntax

```c
void SDL_FlushEvent(Uint32 type);

```

## Function Parameters

|              |                                                                                 |
| ------------ | ------------------------------------------------------------------------------- |
| **type**     | the type of event to be cleared; see [SDL_EventType](SDL_EventType) for details |

## Remarks

This will unconditionally remove any events from the queue that match
`type`. If you need to remove a range of event types, use
[SDL_FlushEvents](SDL_FlushEvents)() instead.

It's also normal to just ignore events you don't care about in your event
loop without calling this function.

This function only affects currently queued events. If you want to make
sure that all pending OS events are flushed, you can call
[SDL_PumpEvents](SDL_PumpEvents)() on the main thread immediately before
the flush call.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_FlushEvents](SDL_FlushEvents)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


