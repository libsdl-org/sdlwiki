###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_JOYSTICK_WGI

A variable controlling whether Windows.Gaming.Input should be used for controller handling.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_WGI "SDL_JOYSTICK_WGI"
```

## Remarks

The variable can be set to the following values:

- "0": WGI is not used.
- "1": WGI is used. (default)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

