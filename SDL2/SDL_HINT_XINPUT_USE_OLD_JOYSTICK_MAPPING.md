###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_XINPUT_USE_OLD_JOYSTICK_MAPPING

A variable that causes SDL to use the old axis and button mapping for XInput devices.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_XINPUT_USE_OLD_JOYSTICK_MAPPING "SDL_XINPUT_USE_OLD_JOYSTICK_MAPPING"
```

## Remarks

This hint is for backwards compatibility only and will be removed in SDL
2.1

The default value is "0". This hint must be set before
[SDL_Init](SDL_Init)()

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

