###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_TIMER_RESOLUTION

A variable that controls the timer resolution, in milliseconds.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

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

The default value is "1".

If this variable is set to "0", the system timer resolution is not set.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

