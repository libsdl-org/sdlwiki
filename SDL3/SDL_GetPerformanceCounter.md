###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetPerformanceCounter

Get the current value of the high resolution counter.

## Syntax

```c
Uint64 SDL_GetPerformanceCounter(void);

```

## Return Value

Returns the current counter value.

## Remarks

This function is typically used for profiling.

The counter values are only meaningful relative to each other. Differences
between values can be converted to times by using
[SDL_GetPerformanceFrequency](SDL_GetPerformanceFrequency.md)().

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_GetPerformanceFrequency](SDL_GetPerformanceFrequency.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryTimer](CategoryTimer.md)
