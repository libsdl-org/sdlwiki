###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_MOUSE_RELATIVE_SCALING

A variable controlling whether relative mouse motion is affected by renderer scaling

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_RELATIVE_SCALING "SDL_MOUSE_RELATIVE_SCALING"
```

## Remarks

This variable can be set to the following values: "0" - Relative motion is
unaffected by DPI or renderer's logical size "1" - Relative motion is
scaled according to DPI scaling and logical size

By default relative mouse deltas are affected by DPI and renderer scaling

## Default

By default relative mouse deltas are affected by DPI and renderer scaling

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)
<!-- #See the Style Guide for instructions on editing the footer. -->


