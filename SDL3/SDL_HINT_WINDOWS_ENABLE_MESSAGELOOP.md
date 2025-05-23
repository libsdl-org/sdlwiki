# SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP

A variable controlling whether the windows message loop is processed by SDL.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP "SDL_WINDOWS_ENABLE_MESSAGELOOP"
```

## Remarks

The variable can be set to the following values:

- "0": The window message loop is not run.
- "1": The window message loop is processed in
  [SDL_PumpEvents](SDL_PumpEvents)(). (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

