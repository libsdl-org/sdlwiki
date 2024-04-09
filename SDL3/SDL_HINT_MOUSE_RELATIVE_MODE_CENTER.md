###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_MOUSE_RELATIVE_MODE_CENTER

A variable controlling whether relative mouse mode constrains the mouse to the center of the window.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_MOUSE_RELATIVE_MODE_CENTER    "SDL_MOUSE_RELATIVE_MODE_CENTER"
```

## Remarks

Constraining to the center of the window works better for FPS games and
when the application is running over RDP. Constraining to the whole window
works better for 2D games and increases the chance that the mouse will be
in the correct position when using high DPI mice.

The variable can be set to the following values:

- "0": Relative mouse mode constrains the mouse to the window.
- "1": Relative mouse mode constrains the mouse to the center of the
  window. (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

