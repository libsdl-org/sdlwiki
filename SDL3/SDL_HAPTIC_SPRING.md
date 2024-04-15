###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HAPTIC_SPRING

Spring effect supported - uses axes position.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HAPTIC_SPRING       (1u<<7)
```

## Remarks

Condition haptic effect that simulates a spring. Effect is based on the
axes position.

## Version

This macro is available since SDL 3.0.0.

## See Also

* [SDL_HapticCondition](SDL_HapticCondition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

