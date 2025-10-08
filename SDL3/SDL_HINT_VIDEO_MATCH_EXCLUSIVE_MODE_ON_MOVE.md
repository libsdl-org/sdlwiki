# SDL_HINT_VIDEO_MATCH_EXCLUSIVE_MODE_ON_MOVE

A variable indicating whether the metal layer drawable size should be updated for the [SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED](SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED) event on macOS.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_MATCH_EXCLUSIVE_MODE_ON_MOVE "SDL_VIDEO_MATCH_EXCLUSIVE_MODE_ON_MOVE"
```

## Remarks

The variable can be set to the following values:

- "0": the metal layer drawable size will not be updated on the
  [SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED](SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED)
  event.
- "1": the metal layer drawable size will be updated on the
  [SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED](SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED)
  event. (default)

This hint should be set before [SDL_Metal_CreateView](SDL_Metal_CreateView)
called.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

