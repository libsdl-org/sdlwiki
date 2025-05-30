# SDL_HINT_JOYSTICK_FLIGHTSTICK_DEVICES

A variable containing a list of flightstick style controllers.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_FLIGHTSTICK_DEVICES "SDL_JOYSTICK_FLIGHTSTICK_DEVICES"
```

## Remarks

The format of the string is a comma separated list of USB VID/PID pairs in
hexadecimal form, e.g.

0xAAAA/0xBBBB,0xCCCC/0xDDDD

The variable can also take the form of @file, in which case the named file
will be loaded and interpreted as the value of the variable.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

