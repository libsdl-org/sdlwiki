# SDL_HINT_RENDER_LINE_METHOD

A variable controlling how the 2D render API renders lines.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_LINE_METHOD "SDL_RENDER_LINE_METHOD"
```

## Remarks

The variable can be set to the following values:

- "0": Use the default line drawing method (Bresenham's line algorithm)
- "1": Use the driver point API using Bresenham's line algorithm (correct,
  draws many points)
- "2": Use the driver line API (occasionally misses line endpoints based on
  hardware driver quirks
- "3": Use the driver geometry API (correct, draws thicker diagonal lines)

This hint should be set before creating a renderer.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

