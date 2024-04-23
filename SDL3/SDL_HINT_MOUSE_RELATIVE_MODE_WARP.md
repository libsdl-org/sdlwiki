###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_MOUSE_RELATIVE_MODE_WARP

A variable controlling whether relative mouse mode is implemented using mouse warping.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_RELATIVE_MODE_WARP    "SDL_MOUSE_RELATIVE_MODE_WARP"
```

## Remarks

The variable can be set to the following values:

- "0": Relative mouse mode uses raw input. (default)
- "1": Relative mouse mode uses mouse warping.

This hint can be set anytime relative mode is not currently enabled.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [[CategoryHints]]
<!-- #See the Style Guide for instructions on editing the footer. -->


