###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_MOUSE_AUTO_CAPTURE

A variable controlling whether the mouse is captured while mouse buttons are pressed

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_MOUSE_AUTO_CAPTURE    "SDL_MOUSE_AUTO_CAPTURE"
```

## Remarks

This variable can be set to the following values: "0" - The mouse is not
captured while mouse buttons are pressed "1" - The mouse is captured while
mouse buttons are pressed

By default the mouse is captured while mouse buttons are pressed so if the
mouse is dragged outside the window, the application continues to receive
mouse events until the button is released.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

