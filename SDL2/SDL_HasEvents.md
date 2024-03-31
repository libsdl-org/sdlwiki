###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HasEvents

Check for the existence of certain event types in the event queue.

## Header File

Defined in [SDL_events.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_events.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
SDL_bool SDL_HasEvents(Uint32 minType, Uint32 maxType);

```

## Function Parameters

|                 |                                                                                                     |
| --------------- | --------------------------------------------------------------------------------------------------- |
| **minType**     | the low end of event type to be queried, inclusive; see [SDL_EventType](SDL_EventType) for details  |
| **maxType**     | the high end of event type to be queried, inclusive; see [SDL_EventType](SDL_EventType) for details |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if events with type >= `minType` and <=
`maxType` are present, or [SDL_FALSE](SDL_FALSE) if not.

## Remarks

If you need to check for a single event type, use
[SDL_HasEvent](SDL_HasEvent)() instead.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_HasEvents](SDL_HasEvents)

----
[CategoryAPI](CategoryAPI)

