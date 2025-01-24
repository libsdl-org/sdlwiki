# SDL_HINT_JOYSTICK_GAMEINPUT

A variable controlling whether GameInput should be used for controller handling on Windows.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_JOYSTICK_GAMEINPUT "SDL_JOYSTICK_GAMEINPUT"
```

## Remarks

The variable can be set to the following values:

- "0": GameInput is not used.
- "1": GameInput is used.

The default is "1" on GDK platforms, and "0" otherwise.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

