# SDL_HINT_VITA_TOUCH_MOUSE_DEVICE

A variable controlling which touchpad should generate synthetic mouse events.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VITA_TOUCH_MOUSE_DEVICE "SDL_VITA_TOUCH_MOUSE_DEVICE"
```

## Remarks

The variable can be set to the following values:

- "0": Only front touchpad should generate mouse events. (default)
- "1": Only back touchpad should generate mouse events.
- "2": Both touchpads should generate mouse events.

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

