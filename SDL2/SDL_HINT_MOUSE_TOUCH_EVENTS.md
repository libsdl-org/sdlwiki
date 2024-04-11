###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_MOUSE_TOUCH_EVENTS

A variable controlling whether mouse events should generate synthetic touch events

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_MOUSE_TOUCH_EVENTS    "SDL_MOUSE_TOUCH_EVENTS"
```

## Remarks

This variable can be set to the following values: "0" - Mouse events will
not generate touch events (default for desktop platforms) "1" - Mouse
events will generate touch events (default for mobile platforms, such as
Android and iOS)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

