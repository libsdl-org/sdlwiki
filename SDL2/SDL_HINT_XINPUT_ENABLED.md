###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_XINPUT_ENABLED

A variable that lets you disable the detection and use of Xinput gamepad devices

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_XINPUT_ENABLED "SDL_XINPUT_ENABLED"
```

## Remarks

The variable can be set to the following values:

- "0": Disable XInput detection (only uses direct input)
- "1": Enable XInput detection (the default)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

