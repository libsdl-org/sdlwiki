###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK

A variable that determines whether ctrl+click should generate a right-click event on Mac

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK "SDL_MAC_CTRL_CLICK_EMULATE_RIGHT_CLICK"
```

## Remarks

If present, holding ctrl while left clicking will generate a right click
event when on Mac.

## Default

By default holding ctrl while left clicking will not generate a right click event when on Mac.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)
<!-- #See the Style Guide for instructions on editing the footer. -->


