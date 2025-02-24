# SDL_HINT_JOYSTICK_HAPTIC_AXES

A variable containing a list of devices and their desired number of haptic (force feedback) enabled axis.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HAPTIC_AXES "SDL_JOYSTICK_HAPTIC_AXES"
```

## Remarks

The format of the string is a comma separated list of USB VID/PID pairs in
hexadecimal form plus the number of desired axes, e.g.

`0xAAAA/0xBBBB/1,0xCCCC/0xDDDD/3`

This hint supports a "wildcard" device that will set the number of haptic
axes on all initialized haptic devices which were not defined explicitly in
this hint.

`0xFFFF/0xFFFF/1`

This hint should be set before a controller is opened. The number of haptic
axes won't exceed the number of real axes found on the device.

## Version

This hint is available since SDL 3.2.5.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

