###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_PEN_DELAY_MOUSE_BUTTON

A variable controlling whether pen mouse button emulation triggers only when the pen touches the tablet surface.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should use `#include <SDL3/SDL.h>`

## Syntax

```c
#define SDL_HINT_PEN_DELAY_MOUSE_BUTTON    "SDL_PEN_DELAY_MOUSE_BUTTON"
```

## Remarks

The variable can be set to the following values:

- "0": The pen reports mouse button press/release immediately when the pen
  button is pressed/released, and the pen tip touching the surface counts
  as left mouse button press.
- "1": Mouse button presses are sent when the pen first touches the tablet
  (analogously for releases). Not pressing a pen button simulates mouse
  button 1, pressing the first pen button simulates mouse button 2 etc.; it
  is not possible to report multiple buttons as pressed at the same time.
  (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

