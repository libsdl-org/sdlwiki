###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_LINUX_HAT_DEADZONES

A variable controlling whether digital hats on Linux will apply deadzones to their underlying input axes or use unfiltered values.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_LINUX_HAT_DEADZONES "SDL_LINUX_HAT_DEADZONES"
```

## Remarks

This variable can be set to the following values:

- "0": Return digital hat values based on unfiltered input axis values
- "1": Return digital hat values with deadzones on the input axes taken
  into account (the default)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

