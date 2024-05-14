###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_RENDER_LINE_METHOD

A variable controlling how the 2D render API renders lines

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_LINE_METHOD "SDL_RENDER_LINE_METHOD"
```

## Remarks

This variable can be set to the following values:

- "0": Use the default line drawing method (Bresenham's line algorithm as
  of SDL 2.0.20)
- "1": Use the driver point API using Bresenham's line algorithm (correct,
  draws many points)
- "2": Use the driver line API (occasionally misses line endpoints based on
  hardware driver quirks, was the default before 2.0.20)
- "3": Use the driver geometry API (correct, draws thicker diagonal lines)

This variable should be set when the renderer is created.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints), [CategoryAPIMacro](CategoryAPIMacro), 

