###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HAPTIC_SPRING

Spring effect supported - uses axes position.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_haptic.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HAPTIC_SPRING     (1u<<7)
```

## Remarks

Condition haptic effect that simulates a spring. Effect is based on the
axes position.

## See Also

* [SDL_HapticCondition](SDL_HapticCondition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

