###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_MAC_FULLSCREEN_SPACES

A variable that specifies the policy for fullscreen Spaces on macOS.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_MAC_FULLSCREEN_SPACES    "SDL_VIDEO_MAC_FULLSCREEN_SPACES"
```

## Remarks

The variable can be set to the following values:

- "0": Disable Spaces support (FULLSCREEN_DESKTOP won't use them and
  [SDL_WINDOW_RESIZABLE](SDL_WINDOW_RESIZABLE) windows won't offer the
  "fullscreen" button on their titlebars).
- "1": Enable Spaces support (FULLSCREEN_DESKTOP will use them and
  [SDL_WINDOW_RESIZABLE](SDL_WINDOW_RESIZABLE) windows will offer the
  "fullscreen" button on their titlebars). (default)

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [[CategoryHints]], [[CategoryDraft]]
<!-- #See the Style Guide for instructions on editing the footer. -->


