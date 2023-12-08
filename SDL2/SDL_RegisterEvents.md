###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_RegisterEvents

Allocate a set of user-defined events, and return the beginning event number for that set of events.

## Syntax

```c
Uint32 SDL_RegisterEvents(int numevents);

```

## Function Parameters

|                   |                                      |
| ----------------- | ------------------------------------ |
| **numevents**     | the number of events to be allocated |

## Return Value

Returns the beginning event number, or (Uint32)-1 if there are not enough
user-defined events left.

## Remarks

Calling this function with `numevents` <= 0 is an error and will return
(Uint32)-1.

Note, (Uint32)-1 means the maximum unsigned 32-bit integer value (or
0xFFFFFFFF), but is clearer to write.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_PushEvent](SDL_PushEvent.md)

----
[CategoryAPI](CategoryAPI.md)
