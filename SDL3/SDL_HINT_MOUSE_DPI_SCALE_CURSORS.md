# SDL_HINT_MOUSE_DPI_SCALE_CURSORS

A variable setting whether we should scale cursors by the current display scale.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_DPI_SCALE_CURSORS "SDL_MOUSE_DPI_SCALE_CURSORS"
```

## Remarks

The variable can be set to the following values:

- "0": Cursors will not change size based on the display content scale.
  (default)
- "1": Cursors will automatically match the display content scale (e.g. a
  2x sized cursor will be used when the window is on a monitor with 200%
  scale). This is currently implemented on Windows and Wayland.

This hint needs to be set before creating cursors.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

