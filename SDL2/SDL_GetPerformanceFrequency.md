###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetPerformanceFrequency

Get the count per second of the high resolution counter.

## Header File

Defined in [SDL_timer.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_timer.h)

## Syntax

```c
Uint64 SDL_GetPerformanceFrequency(void);
```

## Return Value

(Uint64) Returns a platform-specific count per second.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetPerformanceCounter](SDL_GetPerformanceCounter)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)

