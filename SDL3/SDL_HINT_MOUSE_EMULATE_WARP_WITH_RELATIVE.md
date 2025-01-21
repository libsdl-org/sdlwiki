###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_MOUSE_EMULATE_WARP_WITH_RELATIVE

A variable controlling whether warping a hidden mouse cursor will activate relative mouse mode.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_MOUSE_EMULATE_WARP_WITH_RELATIVE "SDL_MOUSE_EMULATE_WARP_WITH_RELATIVE"
```

## Remarks

When this hint is set, the mouse cursor is hidden, and multiple warps to
the window center occur within a short time period, SDL will emulate mouse
warps using relative mouse mode. This can provide smoother and more
reliable mouse motion for some older games, which continuously calculate
the distance travelled by the mouse pointer and warp it back to the center
of the window, rather than using relative mouse motion.

Note that relative mouse mode may have different mouse acceleration
behavior than pointer warps.

If your application needs to repeatedly warp the hidden mouse cursor at a
high-frequency for other purposes, it should disable this hint.

The variable can be set to the following values:

- "0": Attempts to warp the mouse will always be made.
- "1": Some mouse warps will be emulated by forcing relative mouse mode.
  (default)

If not set, this is automatically enabled unless an application uses
relative mouse mode directly.

This hint can be set anytime.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

