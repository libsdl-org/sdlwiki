###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_JOYSTICK_THREAD

A variable controlling whether a separate thread should be used for handling joystick detection and raw input messages on Windows.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_JOYSTICK_THREAD "SDL_JOYSTICK_THREAD"
```

## Remarks

The variable can be set to the following values:

- "0": A separate thread is not used. (default)
- "1": A separate thread is used for handling raw input messages.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

