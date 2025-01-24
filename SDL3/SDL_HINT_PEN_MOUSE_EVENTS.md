# SDL_HINT_PEN_MOUSE_EVENTS

A variable controlling whether pen events should generate synthetic mouse events.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_PEN_MOUSE_EVENTS "SDL_PEN_MOUSE_EVENTS"
```

## Remarks

The variable can be set to the following values:

- "0": Pen events will not generate mouse events.
- "1": Pen events will generate mouse events. (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

