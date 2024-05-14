###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WINDOW_FRAME_USABLE_WHILE_CURSOR_HIDDEN

A variable controlling whether the window frame and title bar are interactive when the cursor is hidden.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOW_FRAME_USABLE_WHILE_CURSOR_HIDDEN    "SDL_WINDOW_FRAME_USABLE_WHILE_CURSOR_HIDDEN"
```

## Remarks

The variable can be set to the following values:

- "0": The window frame is not interactive when the cursor is hidden (no
  move, resize, etc).
- "1": The window frame is interactive when the cursor is hidden. (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

