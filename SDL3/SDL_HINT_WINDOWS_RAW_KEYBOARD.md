###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WINDOWS_RAW_KEYBOARD

A variable controlling whether raw keyboard events are used on Windows.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_RAW_KEYBOARD   "SDL_WINDOWS_RAW_KEYBOARD"
```

## Remarks

The variable can be set to the following values:

- "0": The Windows message loop is used for keyboard events.
- "1": Low latency raw keyboard events are used. (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

