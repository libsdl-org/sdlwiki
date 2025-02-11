# SDL_HINT_JOYSTICK_HIDAPI_XBOX

A variable controlling whether the HIDAPI driver for XBox controllers should be used.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_XBOX   "SDL_JOYSTICK_HIDAPI_XBOX"
```

## Remarks

This variable can be set to the following values:

- "0": HIDAPI driver is not used
- "1": HIDAPI driver is used

The default is "0" on Windows, otherwise the value of
[SDL_HINT_JOYSTICK_HIDAPI](SDL_HINT_JOYSTICK_HIDAPI)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

