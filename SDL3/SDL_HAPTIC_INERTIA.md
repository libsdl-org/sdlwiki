###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HAPTIC_INERTIA

Inertia effect supported - uses axes acceleration.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HAPTIC_INERTIA      (1u<<9)
```

## Remarks

Condition haptic effect that simulates inertia. Effect is based on the axes
acceleration.

## Version

This macro is available since SDL 3.0.0.

## See Also

* [SDL_HapticCondition](SDL_HapticCondition)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

