###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HAPTIC_DAMPER

Damper effect supported - uses axes velocity.

## Header File

Defined in [<SDL3/SDL_haptic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h)

## Syntax

```c
#define SDL_HAPTIC_DAMPER       (1u<<8)
```

## Remarks

Condition haptic effect that simulates dampening. Effect is based on the
axes velocity.

## Version

This macro is available since SDL 3.0.0.

## See Also

* [SDL_HapticCondition](SDL_HapticCondition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

