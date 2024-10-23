###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_JOYSTICK_HIDAPI_PS5

A variable controlling whether the HIDAPI driver for PS5 controllers should be used.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_PS5 "SDL_JOYSTICK_HIDAPI_PS5"
```

## Remarks

The variable can be set to the following values:

- "0": HIDAPI driver is not used.
- "1": HIDAPI driver is used.

The default is the value of
[SDL_HINT_JOYSTICK_HIDAPI](SDL_HINT_JOYSTICK_HIDAPI).

This hint should be set before enumerating controllers.

## Version

This hint is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

