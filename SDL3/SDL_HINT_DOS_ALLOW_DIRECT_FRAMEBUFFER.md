# SDL_HINT_DOS_ALLOW_DIRECT_FRAMEBUFFER

A variable that enables a fast framebuffer path on DOS.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_DOS_ALLOW_DIRECT_FRAMEBUFFER "SDL_DOS_ALLOW_DIRECT_FRAMEBUFFER"
```

## Remarks

When set to "1", [SDL_UpdateWindowSurface](SDL_UpdateWindowSurface)()
copies the system-RAM surface directly to VRAM and skips software cursor
compositing and vsync.

The variable can be set to the following values:

- "0": Use the normal path with cursor compositing and vsync. (default)
- "1": Use the fast direct-to-VRAM path when available.

This hint must be set before the first call to
[SDL_GetWindowSurface](SDL_GetWindowSurface)().

## Version

This hint is available since SDL 3.6.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

