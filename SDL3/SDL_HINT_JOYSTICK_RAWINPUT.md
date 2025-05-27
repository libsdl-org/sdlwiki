# SDL_HINT_JOYSTICK_RAWINPUT

A variable controlling whether the RAWINPUT joystick drivers should be used for better handling XInput-capable devices.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_RAWINPUT "SDL_JOYSTICK_RAWINPUT"
```

## Remarks

The variable can be set to the following values:

- "0": RAWINPUT drivers are not used. (default)
- "1": RAWINPUT drivers are used.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

