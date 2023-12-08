###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

This function is available since SDL 3.0.0.

## Code Examples

<<Include([SDL_UserEvent](SDL_UserEvent.md), , , from="== Code Examples ==", to="== Remarks ==")>>

## Related Functions

* [SDL_PushEvent](SDL_PushEvent.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryEvents](CategoryEvents.md)
