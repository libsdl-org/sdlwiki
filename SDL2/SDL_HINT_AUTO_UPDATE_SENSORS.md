# SDL_HINT_AUTO_UPDATE_SENSORS

A variable controlling whether SDL updates sensor state when getting input events

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUTO_UPDATE_SENSORS    "SDL_AUTO_UPDATE_SENSORS"
```

## Remarks

This variable can be set to the following values:

- "0": You'll call [SDL_SensorUpdate](SDL_SensorUpdate)() manually
- "1": SDL will automatically call [SDL_SensorUpdate](SDL_SensorUpdate)()
  (default)

This hint can be toggled on and off at runtime.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

