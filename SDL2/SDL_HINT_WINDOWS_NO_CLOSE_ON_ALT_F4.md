###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)

## Draft

**THIS PAGE IS A WORK IN PROGRESS** ... Please make edits to this page to improve it!


<!-- #*^*^*^*^*See https://wiki.libsdl.org/SGEnumerations for details on editing this page*^*^*^*^* -->
# SDL_HINT_WINDOWS_NO_CLOSE_ON_ALT_F4

Tell SDL not to generate window-close events for Alt+F4 on Windows.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_WINDOWS_NO_CLOSE_ON_ALT_F4 "SDL_WINDOWS_NO_CLOSE_ON_ALT_F4"
```

## Remarks

The variable can be set to the following values: "0" - SDL will generate a
window-close event when it sees Alt+F4. "1" - SDL will only do normal key
handling for Alt+F4.

## Default

By default SDL will generate an [[SDL_WindowEvent|SDL_WINDOWEVENT_CLOSE]] event for Alt+F4.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints), [CategoryDraft](CategoryDraft)
<!-- #See the Style Guide for instructions on editing the footer. -->


