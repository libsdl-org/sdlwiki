###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_TOUCH_MOUSE_EVENTS

A variable controlling whether touch events should generate synthetic mouse events

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_TOUCH_MOUSE_EVENTS    "SDL_TOUCH_MOUSE_EVENTS"
```

## Remarks

This variable can be set to the following values:

- "0": Touch events will not generate mouse events
- "1": Touch events will generate mouse events

By default SDL will generate mouse events for touch events

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

