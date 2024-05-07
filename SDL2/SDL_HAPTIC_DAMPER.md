###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HAPTIC_DAMPER

Damper effect supported - uses axes velocity.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h)

## Syntax

```c
#define SDL_HAPTIC_DAMPER     (1u<<8)
```

## Remarks

Condition haptic effect that simulates dampening. Effect is based on the
axes velocity.

## See Also

- [SDL_HapticCondition](SDL_HapticCondition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

