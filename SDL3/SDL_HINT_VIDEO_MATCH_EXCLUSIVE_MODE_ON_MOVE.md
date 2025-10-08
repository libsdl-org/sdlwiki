# SDL_HINT_VIDEO_MATCH_EXCLUSIVE_MODE_ON_MOVE

A variable controlling whether SDL will attempt to automatically set the destination display to a mode most closely matching that of the previous display if an exclusive fullscreen window is moved onto it.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_MATCH_EXCLUSIVE_MODE_ON_MOVE "SDL_VIDEO_MATCH_EXCLUSIVE_MODE_ON_MOVE"
```

## Remarks

The variable can be set to the following values:

- "0": SDL will not attempt to automatically set a matching mode on the
  destination display. If an exclusive fullscreen window is moved to a new
  display, the window will become fullscreen desktop.
- "1": SDL will attempt to automatically set a mode on the destination
  display that most closely matches the mode of the display that the
  exclusive fullscreen window was previously on. (default)

This hint can be set anytime.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

