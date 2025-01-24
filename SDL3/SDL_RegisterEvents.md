# SDL_RegisterEvents

Allocate a set of user-defined events, and return the beginning event number for that set of events.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
Uint32 SDL_RegisterEvents(int numevents);
```

## Function Parameters

|     |               |                                       |
| --- | ------------- | ------------------------------------- |
| int | **numevents** | the number of events to be allocated. |

## Return Value

([Uint32](Uint32)) Returns the beginning event number, or 0 if numevents is
invalid or if there are not enough user-defined events left.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_PushEvent](SDL_PushEvent)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)

