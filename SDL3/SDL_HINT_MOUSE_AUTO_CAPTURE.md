###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_MOUSE_AUTO_CAPTURE

A variable controlling whether the mouse is captured while mouse buttons are pressed.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_AUTO_CAPTURE    "SDL_MOUSE_AUTO_CAPTURE"
```

## Remarks

The variable can be set to the following values:

- "0": The mouse is not captured while mouse buttons are pressed.
- "1": The mouse is captured while mouse buttons are pressed.

By default the mouse is captured while mouse buttons are pressed so if the
mouse is dragged outside the window, the application continues to receive
mouse events until the button is released.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

