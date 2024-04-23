###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_LINUX_JOYSTICK_CLASSIC

A variable controlling whether to use the classic /dev/input/js* joystick interface or the newer /dev/input/event* joystick interface on Linux

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_LINUX_JOYSTICK_CLASSIC "SDL_LINUX_JOYSTICK_CLASSIC"
```

## Remarks

This variable can be set to the following values:

- "0": Use /dev/input/event*
- "1": Use /dev/input/js*

By default the /dev/input/event* interfaces are used

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

