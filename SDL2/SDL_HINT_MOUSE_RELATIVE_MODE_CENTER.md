###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_MOUSE_RELATIVE_MODE_CENTER

A variable controlling whether relative mouse mode constrains the mouse to the center of the window

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_RELATIVE_MODE_CENTER    "SDL_MOUSE_RELATIVE_MODE_CENTER"
```

## Remarks

This variable can be set to the following values: "0" - Relative mouse mode
constrains the mouse to the window "1" - Relative mouse mode constrains the
mouse to the center of the window

Constraining to the center of the window works better for FPS games and
when the application is running over RDP. Constraining to the whole window
works better for 2D games and increases the chance that the mouse will be
in the correct position when using high DPI mice.

By default SDL will constrain the mouse to the center of the window

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

