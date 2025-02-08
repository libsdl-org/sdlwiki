# SDL_HINT_QTWAYLAND_WINDOW_FLAGS

Flags to set on QtWayland windows to integrate with the native window manager.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_QTWAYLAND_WINDOW_FLAGS "SDL_QTWAYLAND_WINDOW_FLAGS"
```

## Remarks

On QtWayland platforms, this hint controls the flags to set on the windows.
For example, on Sailfish OS "OverridesSystemGestures" disables swipe
gestures.

This variable is a space-separated list of the following values (empty = no
flags):

- "OverridesSystemGestures"
- "StaysOnTop"
- "BypassWindowManager"

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

