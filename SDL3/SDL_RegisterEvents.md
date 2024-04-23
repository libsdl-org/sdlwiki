###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_RegisterEvents

Allocate a set of user-defined events, and return the beginning event number for that set of events.

## Header File

Defined in [<SDL3/SDL_events.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_events.h)

## Syntax

```c
Uint32 SDL_RegisterEvents(int numevents);

```

## Function Parameters

|                   |                                      |
| ----------------- | ------------------------------------ |
| **numevents**     | the number of events to be allocated |

## Return Value

Returns the beginning event number, or 0 if numevents is invalid or if
there are not enough user-defined events left.

## Version

This function is available since SDL 3.0.0.

## Code Examples

<<Include([SDL_UserEvent](SDL_UserEvent), , , from="== Code Examples ==", to="== Remarks ==")>>

## See Also

* [SDL_PushEvent](SDL_PushEvent)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryEvents](CategoryEvents)


