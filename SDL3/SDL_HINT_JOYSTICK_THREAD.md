# SDL_HINT_JOYSTICK_THREAD

A variable controlling whether a separate thread should be used for handling joystick detection and raw input messages on Windows.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_THREAD "SDL_JOYSTICK_THREAD"
```

## Remarks

The variable can be set to the following values:

- "0": A separate thread is not used.
- "1": A separate thread is used for handling raw input messages. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

