###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_PeepEvents

Check the event queue for messages and optionally return them.

## Syntax

```c
int SDL_PeepEvents(SDL_Event * events, int numevents,
                   SDL_eventaction action,
                   Uint32 minType, Uint32 maxType);

```

## Function Parameters

|                   |                                                                                                                                                                                                                       |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **events**        | destination buffer for the retrieved events                                                                                                                                                                           |
| **numevents**     | if action is [SDL_ADDEVENT](SDL_ADDEVENT), the number of events to add back to the event queue; if action is [SDL_PEEKEVENT](SDL_PEEKEVENT) or [SDL_GETEVENT](SDL_GETEVENT), the maximum number of events to retrieve |
| **action**        | action to take; see [[#action|Remarks]] for details                                                                                                                                                                   |
| **minType**       | minimum value of the event type to be considered; [SDL_EVENT_FIRST](SDL_EVENT_FIRST) is a safe choice                                                                                                                 |
| **maxType**       | maximum value of the event type to be considered; [SDL_EVENT_LAST](SDL_EVENT_LAST) is a safe choice                                                                                                                   |

## Return Value

Returns the number of events actually stored or a negative error code on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

`action` may be any of the following:

- [`SDL_ADDEVENT`](SDL_ADDEVENT): up to `numevents` events will be added to
  the back of the event queue.
- [`SDL_PEEKEVENT`](SDL_PEEKEVENT): `numevents` events at the front of the
  event queue, within the specified minimum and maximum type, will be
  returned to the caller and will _not_ be removed from the queue.
- [`SDL_GETEVENT`](SDL_GETEVENT): up to `numevents` events at the front of
  the event queue, within the specified minimum and maximum type, will be
  returned to the caller and will be removed from the queue.

You may have to call [SDL_PumpEvents](SDL_PumpEvents)() before calling this
function. Otherwise, the events may not be ready to be filtered when you
call [SDL_PeepEvents](SDL_PeepEvents)().

This function is thread-safe.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
Add a code example here.
```

## Related Functions

* [SDL_PollEvent](SDL_PollEvent)
* [SDL_PumpEvents](SDL_PumpEvents)
* [SDL_PushEvent](SDL_PushEvent)

----
[CategoryAPI](CategoryAPI), [CategoryEvents](CategoryEvents)


