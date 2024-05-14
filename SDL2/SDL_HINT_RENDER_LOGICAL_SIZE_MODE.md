###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_RENDER_LOGICAL_SIZE_MODE

A variable controlling the scaling policy for [SDL_RenderSetLogicalSize](SDL_RenderSetLogicalSize).

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_LOGICAL_SIZE_MODE       "SDL_RENDER_LOGICAL_SIZE_MODE"
```

## Remarks

This variable can be set to the following values:

"0" or "letterbox" - Uses letterbox/sidebars to fit the entire rendering on
screen "1" or "overscan" - Will zoom the rendering so it fills the entire
screen, allowing edges to be drawn offscreen

By default letterbox is used

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

