# SDL_HINT_GAMECONTROLLER_IGNORE_DEVICES_EXCEPT

If set, all devices will be skipped when scanning for game controllers except for the ones listed in this variable.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_GAMECONTROLLER_IGNORE_DEVICES_EXCEPT "SDL_GAMECONTROLLER_IGNORE_DEVICES_EXCEPT"
```

## Remarks

The format of the string is a comma separated list of USB VID/PID pairs in
hexadecimal form, e.g.

0xAAAA/0xBBBB,0xCCCC/0xDDDD

The variable can also take the form of @file, in which case the named file
will be loaded and interpreted as the value of the variable.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

