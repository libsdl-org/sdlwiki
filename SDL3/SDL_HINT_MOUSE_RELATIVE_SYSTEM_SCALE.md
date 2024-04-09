###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_MOUSE_RELATIVE_SYSTEM_SCALE

A variable controlling whether the system mouse acceleration curve is used for relative mouse motion.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_MOUSE_RELATIVE_SYSTEM_SCALE    "SDL_MOUSE_RELATIVE_SYSTEM_SCALE"
```

## Remarks

The variable can be set to the following values:

- "0": Relative mouse motion will be unscaled. (default)
- "1": Relative mouse motion will be scaled using the system mouse
  acceleration curve.

If
[SDL_HINT_MOUSE_RELATIVE_SPEED_SCALE](SDL_HINT_MOUSE_RELATIVE_SPEED_SCALE)
is set, that will override the system speed scale.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

