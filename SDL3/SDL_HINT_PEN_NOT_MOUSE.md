###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_PEN_NOT_MOUSE

A variable controlling whether to treat pen movement as separate from mouse movement.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_PEN_NOT_MOUSE    "SDL_PEN_NOT_MOUSE"
```

## Remarks

By default, pens report both [SDL_MouseMotionEvent](SDL_MouseMotionEvent)
and [SDL_PenMotionEvent](SDL_PenMotionEvent) updates (analogously for
button presses). This hint allows decoupling mouse and pen updates.

This variable toggles between the following behaviour:

- "0": Pen acts as a mouse with mouse ID
  [SDL_PEN_MOUSEID](SDL_PEN_MOUSEID). (default) Use case: client
  application is not pen aware, user wants to use pen instead of mouse to
  interact.
- "1": Pen reports mouse clicks and movement events but does not update
  SDL-internal mouse state (buttons pressed, current mouse location). Use
  case: client application is not pen aware, user frequently alternates
  between pen and "real" mouse.
- "2": Pen reports no mouse events. Use case: pen-aware client application
  uses this hint to allow user to toggle between pen+mouse mode ("2") and
  pen-only mode ("1" or "0").

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

