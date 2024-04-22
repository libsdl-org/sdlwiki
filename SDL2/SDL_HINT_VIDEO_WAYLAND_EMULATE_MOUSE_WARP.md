###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_WAYLAND_EMULATE_MOUSE_WARP

Enable or disable mouse pointer warp emulation, needed by some older games.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_WAYLAND_EMULATE_MOUSE_WARP "SDL_VIDEO_WAYLAND_EMULATE_MOUSE_WARP"
```

## Remarks

When this hint is set, any SDL will emulate mouse warps using relative
mouse mode. This is required for some older games (such as Source engine
games), which warp the mouse to the centre of the screen rather than using
relative mouse motion. Note that relative mouse mode may have different
mouse acceleration behaviour than pointer warps.

This variable can be set to the following values: "0" - All mouse warps
fail, as mouse warping is not available under wayland. "1" - Some mouse
warps will be emulated by forcing relative mouse mode.

If not set, this is automatically enabled unless an application uses
relative mouse mode directly.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

