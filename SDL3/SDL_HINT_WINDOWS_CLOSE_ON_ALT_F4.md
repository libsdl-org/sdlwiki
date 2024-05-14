###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WINDOWS_CLOSE_ON_ALT_F4

A variable controlling whether SDL generates window-close events for Alt+F4 on Windows.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_CLOSE_ON_ALT_F4 "SDL_WINDOWS_CLOSE_ON_ALT_F4"
```

## Remarks

The variable can be set to the following values:

- "0": SDL will only do normal key handling for Alt+F4.
- "1": SDL will generate a window-close event when it sees Alt+F4.
  (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

