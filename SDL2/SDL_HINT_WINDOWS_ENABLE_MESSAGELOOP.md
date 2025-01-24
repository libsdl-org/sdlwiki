# SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP

A variable controlling whether the windows message loop is processed by SDL

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_ENABLE_MESSAGELOOP "SDL_WINDOWS_ENABLE_MESSAGELOOP"
```

## Remarks

This variable can be set to the following values:

- "0": The window message loop is not run
- "1": The window message loop is processed in
  [SDL_PumpEvents](SDL_PumpEvents)()

By default SDL will process the windows message loop





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

