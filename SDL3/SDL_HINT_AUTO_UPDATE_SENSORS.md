# SDL_HINT_AUTO_UPDATE_SENSORS

A variable controlling whether SDL updates sensor state when getting input events.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_AUTO_UPDATE_SENSORS "SDL_AUTO_UPDATE_SENSORS"
```

## Remarks

The variable can be set to the following values:

- "0": You'll call [SDL_UpdateSensors](SDL_UpdateSensors)() manually.
- "1": SDL will automatically call
  [SDL_UpdateSensors](SDL_UpdateSensors)(). (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

