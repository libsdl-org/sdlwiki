###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_GAMECONTROLLERTYPE

A variable that overrides the automatic controller type detection

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_GAMECONTROLLERTYPE "SDL_GAMECONTROLLERTYPE"
```

## Remarks

The variable should be comma separated entries, in the form: VID/PID=type

The VID and PID should be hexadecimal with exactly 4 digits, e.g. 0x00fd

The type should be one of: Xbox360 XboxOne PS3 PS4 PS5 SwitchPro

This hint affects what driver is used, and must be set before calling
[SDL_Init](SDL_Init)([SDL_INIT_GAMECONTROLLER](SDL_INIT_GAMECONTROLLER))

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

