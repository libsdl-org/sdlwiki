# SDL_HINT_WINDOWS_RAW_MOUSE_NOLEGACY

A variable controlling whether the RIDEV_NOLEGACY flag is set when enabling Windows raw mouse events.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_RAW_MOUSE_NOLEGACY "SDL_WINDOWS_RAW_MOUSE_NOLEGACY"
```

## Remarks

If RIDEV_NOLEGACY is set, then Windows mouse events will not be sent for
mouse motion while relative mode is enabled. This improves performance when
players are using high DPI mice, but should be disabled while showing
custom assert dialogs in your application code.

Caution: Windows will not see mouse button releases in relative mode with
this active. This means you should not enable relative mode while a mouse
button is currently pressed.

- "0": Windows mouse events will be generated while relative motion is
  enabled. (default)
- "1": Windows mouse events will not be generated while relative motion is
  enabled.

This hint can be set anytime.

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

