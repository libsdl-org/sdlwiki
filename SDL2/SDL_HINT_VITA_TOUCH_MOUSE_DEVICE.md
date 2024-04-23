###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VITA_TOUCH_MOUSE_DEVICE

A variable controlling which touchpad should generate synthetic mouse events

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VITA_TOUCH_MOUSE_DEVICE    "SDL_HINT_VITA_TOUCH_MOUSE_DEVICE"
```

## Remarks

This variable can be set to the following values:

- "0": Only front touchpad should generate mouse events. Default
- "1": Only back touchpad should generate mouse events.
- "2": Both touchpads should generate mouse events.

By default SDL will generate mouse events for all touch devices

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

