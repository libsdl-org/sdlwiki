###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_LINUX_DIGITAL_HATS

A variable controlling whether joysticks on Linux will always treat 'hat' axis inputs (ABS_HAT0X - ABS_HAT3Y) as 8-way digital hats without checking whether they may be analog.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_LINUX_DIGITAL_HATS "SDL_LINUX_DIGITAL_HATS"
```

## Remarks

This variable can be set to the following values: "0" - Only map hat axis
inputs to digital hat outputs if the input axes appear to actually be
digital (the default) "1" - Always handle the input axes numbered ABS_HAT0X
to ABS_HAT3Y as digital hats

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

