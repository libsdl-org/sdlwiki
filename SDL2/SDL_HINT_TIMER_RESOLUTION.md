###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_TIMER_RESOLUTION

A variable that controls the timer resolution, in milliseconds.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_TIMER_RESOLUTION "SDL_TIMER_RESOLUTION"
```

## Remarks

The higher resolution the timer, the more frequently the CPU services timer
interrupts, and the more precise delays are, but this takes up power and
CPU time. This hint is only used on Windows.

See this blog post for more information:
http://randomascii.wordpress.com/2013/07/08/windows-timer-resolution-megawatts-wasted/

If this variable is set to "0", the system timer resolution is not set.

The default value is "1". This hint may be set at any time.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints), [CategoryAPIMacro](CategoryAPIMacro), 


