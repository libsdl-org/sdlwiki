# SDL_HINT_PEN_TOUCH_EVENTS

A variable controlling whether pen events should generate synthetic touch events.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_PEN_TOUCH_EVENTS "SDL_PEN_TOUCH_EVENTS"
```

## Remarks

The variable can be set to the following values:

- "0": Pen events will not generate touch events.
- "1": Pen events will generate touch events. (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

