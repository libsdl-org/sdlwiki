###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TomerCallback

The callback function for SDL_AddTimer.

## Syntax

```c
Uint32 (*SDL_TimerCallback)(Uint32 interval, void *param);

```

## Function Parameters

|                  |                                                                                                   |
| ---------------- | ------------------------------------------------------------------------------------------------- |
| **interval**     | the timer delay, in milliseconds, passed by SDL_AddTimer                                          |
| **param**        | a pointer that is passed by SDL_AddTimer                                                          |

## Return Value

Returns the next timer interval. If 0, the timer is cancelled.

## Remarks

See SDL_AddTimer

## Version

This function is available since SDL 3.0.0.

## Code Examples

See SDL_AddTimer

## Related Functions

* [SDL_AddTimer](SDL_AddTimer)

----
[CategoryAPI](CategoryAPI), [CategoryTimer](CategoryTimer)


