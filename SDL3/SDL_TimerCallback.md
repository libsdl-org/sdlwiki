###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TimerCallback

Function prototype for the timer callback function.

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h)

## Syntax

```c
typedef Uint32 (SDLCALL *SDL_TimerCallback)(Uint32 interval, void *param);
```

## Function Parameters

|                  |                                                                                                 |
| ---------------- | ----------------------------------------------------------------------------------------------- |
| **interval**     | the current callback time interval.                                                             |
| **param**        | an arbitrary pointer provided by the app through [SDL_AddTimer](SDL_AddTimer), for its own use. |

## Return Value

Returns the new callback time interval, or 0 to disable further runs of the
callback.

## Remarks

The callback function is passed the current timer interval and returns the
next timer interval, in milliseconds. If the returned value is the same as
the one passed in, the periodic alarm continues, otherwise a new alarm is
scheduled. If the callback returns 0, the periodic alarm is cancelled.

## Thread Safety

SDL may call this callback at any time from a background thread; the
application is responsible for locking resources the callback touches that
need to be protected.

## Version

This datatype is available since SDL 3.0.0.

## See Also

* [SDL_AddTimer](SDL_AddTimer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryTimer](CategoryTimer)


