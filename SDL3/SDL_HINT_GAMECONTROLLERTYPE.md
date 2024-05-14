###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_GAMECONTROLLERTYPE

A variable that overrides the automatic controller type detection.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_GAMECONTROLLERTYPE "SDL_GAMECONTROLLERTYPE"
```

## Remarks

The variable should be comma separated entries, in the form: VID/PID=type

The VID and PID should be hexadecimal with exactly 4 digits, e.g. 0x00fd

This hint affects what low level protocol is used with the HIDAPI driver.

The variable can be set to the following values:

- "Xbox360"
- "XboxOne"
- "PS3"
- "PS4"
- "PS5"
- "SwitchPro"

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

