###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!



<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGEnumerations for details on editing this page*^*^*^*^* -->
# SDL_HINT_MOUSE_FOCUS_CLICKTHROUGH

Allow mouse click events when clicking to focus an SDL window

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_FOCUS_CLICKTHROUGH "SDL_MOUSE_FOCUS_CLICKTHROUGH"
```

## Remarks

This variable can be set to the following values: "0" - Ignore mouse clicks
that activate a window "1" - Generate events for mouse clicks that activate
a window

By default SDL will ignore mouse clicks that activate a window

## Default

By default no mouse click events are sent when clicking to focus.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


