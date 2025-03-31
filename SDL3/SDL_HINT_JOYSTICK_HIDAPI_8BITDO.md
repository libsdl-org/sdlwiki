# SDL_HINT_JOYSTICK_HIDAPI_8BITDO

A variable controlling whether the HIDAPI driver for 8BitDo controllers should be used.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_HIDAPI_8BITDO "SDL_JOYSTICK_HIDAPI_8BITDO"
```

## Remarks

This variable can be set to the following values:

"0" - HIDAPI driver is not used. "1" - HIDAPI driver is used.

The default is the value of
[SDL_HINT_JOYSTICK_HIDAPI](SDL_HINT_JOYSTICK_HIDAPI)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

