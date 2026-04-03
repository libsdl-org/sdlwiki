# SDL_HINT_JOYSTICK_GAMEINPUT_RAW

A variable controlling whether GameInput should be used for handling GIP devices that require raw report processing, but aren't supported by HIDRAW, such as Xbox One Guitars.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_GAMEINPUT_RAW "SDL_JOYSTICK_GAMEINPUT_RAW"
```

## Remarks

Note that this is only supported with GameInput 3 or newer.

The variable can be set to the following values:

- "0": GameInput is not used to handle raw GIP devices.
- "1": GameInput is used.

The default is "1" when using GameInput 3 or newer, and is "0" otherwise.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.4.4.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

