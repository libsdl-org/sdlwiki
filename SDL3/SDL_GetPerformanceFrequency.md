###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetPerformanceFrequency

Get the count per second of the high resolution counter.

## Header File

Defined in [<SDL3/SDL_timer.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_timer.h)

## Syntax

```c
Uint64 SDL_GetPerformanceFrequency(void);
```

## Return Value

(Uint64) Returns a platform-specific count per second.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetPerformanceCounter](SDL_GetPerformanceCounter)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryTimer](CategoryTimer)

