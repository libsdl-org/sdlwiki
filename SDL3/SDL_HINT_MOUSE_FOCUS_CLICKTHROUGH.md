# SDL_HINT_MOUSE_FOCUS_CLICKTHROUGH

Allow mouse click events when clicking to focus an SDL window.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_FOCUS_CLICKTHROUGH "SDL_MOUSE_FOCUS_CLICKTHROUGH"
```

## Remarks

The variable can be set to the following values:

- "0": Ignore mouse clicks that activate a window. (default)
- "1": Generate events for mouse clicks that activate a window.

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

