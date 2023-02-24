###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_FlushEvent

Clear events of a specific type from the event queue.

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_FlushEvents](SDL_FlushEvents)

----
[CategoryAPI](CategoryAPI), [CategoryEvents](CategoryEvents)


