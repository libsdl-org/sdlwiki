# SDL_HINT_VIDEO_MINIMIZE_ON_FOCUS_LOSS

A variable controlling whether fullscreen windows are minimized when they lose focus.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_MINIMIZE_ON_FOCUS_LOSS "SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS"
```

## Remarks

The variable can be set to the following values:

- "0": Fullscreen windows will not be minimized when they lose focus.
- "1": Fullscreen windows are minimized when they lose focus.
- "auto": Fullscreen windows are minimized when they lose focus if they use
  exclusive fullscreen modes, so the desktop video mode is restored.
  (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

