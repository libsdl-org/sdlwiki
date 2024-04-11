###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_JOYSTICK_THREAD

A variable controlling whether a separate thread should be used for handling joystick detection and raw input messages on Windows

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_JOYSTICK_THREAD "SDL_JOYSTICK_THREAD"
```

## Remarks

This variable can be set to the following values: "0" - A separate thread
is not used (the default) "1" - A separate thread is used for handling raw
input messages

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

