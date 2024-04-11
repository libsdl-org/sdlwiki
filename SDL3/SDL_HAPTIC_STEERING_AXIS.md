###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HAPTIC_STEERING_AXIS

Use this value to play an effect on the steering wheel axis.

## Header File

Defined in [SDL_haptic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_haptic.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HAPTIC_STEERING_AXIS 3
```

## Remarks

This provides better compatibility across platforms and devices as SDL will
guess the correct axis.

## Version

This macro is available since SDL 3.0.0.

## See Also

* [SDL_HapticDirection](SDL_HapticDirection)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

