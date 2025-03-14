# SDL_HINT_JOYSTICK_LINUX_CLASSIC

A variable controlling whether to use the classic /dev/input/js* joystick interface or the newer /dev/input/event* joystick interface on Linux.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_LINUX_CLASSIC "SDL_JOYSTICK_LINUX_CLASSIC"
```

## Remarks

The variable can be set to the following values:

- "0": Use /dev/input/event* (default)
- "1": Use /dev/input/js*

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

