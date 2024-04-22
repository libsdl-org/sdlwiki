###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_DISPLAY_USABLE_BOUNDS

Override for [SDL_GetDisplayUsableBounds](SDL_GetDisplayUsableBounds)().

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_DISPLAY_USABLE_BOUNDS "SDL_DISPLAY_USABLE_BOUNDS"
```

## Remarks

If set, this hint will override the expected results for
[SDL_GetDisplayUsableBounds](SDL_GetDisplayUsableBounds)() for display
index 0. Generally you don't want to do this, but this allows an embedded
system to request that some of the screen be reserved for other uses when
paired with a well-behaved application.

The contents of this hint must be 4 comma-separated integers, the first is
the bounds x, then y, width and height, in that order.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

