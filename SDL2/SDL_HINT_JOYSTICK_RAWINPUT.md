# SDL_HINT_JOYSTICK_RAWINPUT

A variable controlling whether the RAWINPUT joystick drivers should be used for better handling XInput-capable devices.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_RAWINPUT "SDL_JOYSTICK_RAWINPUT"
```

## Remarks

This variable can be set to the following values:

- "0": RAWINPUT drivers are not used (the default)
- "1": RAWINPUT drivers are used

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

