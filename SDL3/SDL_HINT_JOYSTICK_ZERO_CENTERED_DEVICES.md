# SDL_HINT_JOYSTICK_ZERO_CENTERED_DEVICES

A variable containing a list of devices known to have all axes centered at zero.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_ZERO_CENTERED_DEVICES "SDL_JOYSTICK_ZERO_CENTERED_DEVICES"
```

## Remarks

The format of the string is a comma separated list of USB VID/PID pairs in
hexadecimal form, e.g.

`0xAAAA/0xBBBB,0xCCCC/0xDDDD`

The variable can also take the form of "@file", in which case the named
file will be loaded and interpreted as the value of the variable.

This hint should be set before a controller is opened.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

