###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_WAYLAND_EMULATE_MOUSE_WARP

Enable or disable hidden mouse pointer warp emulation, needed by some older games.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_WAYLAND_EMULATE_MOUSE_WARP "SDL_VIDEO_WAYLAND_EMULATE_MOUSE_WARP"
```

## Remarks

Wayland requires the pointer confinement protocol to warp the mouse, but
that is just a hint that the compositor is free to ignore, and warping the
the pointer to or from regions outside of the focused window is prohibited.
When this hint is set and the pointer is hidden, SDL will emulate mouse
warps using relative mouse mode. This is required for some older games
(such as Source engine games), which warp the mouse to the centre of the
screen rather than using relative mouse motion. Note that relative mouse
mode may have different mouse acceleration behaviour than pointer warps.

The variable can be set to the following values:

- "0": Attempts to warp the mouse will be made, if the appropriate protocol
  is available.
- "1": Some mouse warps will be emulated by forcing relative mouse mode.

If not set, this is automatically enabled unless an application uses
relative mouse mode directly.

This hint can be set anytime.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

