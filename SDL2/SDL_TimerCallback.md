###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_TimerCallback

Function prototype for the timer callback function.

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_timer.h)

## Syntax

```c
typedef Uint32 (SDLCALL * SDL_TimerCallback) (Uint32 interval, void *param);
```

## Remarks

The callback function is passed the current timer interval and returns the
next timer interval. If the returned value is the same as the one passed
in, the periodic alarm continues, otherwise a new alarm is scheduled. If
the callback returns 0, the periodic alarm is cancelled.

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryTimer](CategoryTimer)

