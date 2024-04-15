###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_JOYSTICK_LINUX_HAT_DEADZONES

A variable controlling whether digital hats on Linux will apply deadzones to their underlying input axes or use unfiltered values.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_JOYSTICK_LINUX_HAT_DEADZONES "SDL_JOYSTICK_LINUX_HAT_DEADZONES"
```

## Remarks

The variable can be set to the following values:

- "0": Return digital hat values based on unfiltered input axis values.
- "1": Return digital hat values with deadzones on the input axes taken
  into account. (default)

This hint should be set before a controller is opened.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

