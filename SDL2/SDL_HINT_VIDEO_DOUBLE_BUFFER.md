###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_DOUBLE_BUFFER

Tell the video driver that we only want a double buffer.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_DOUBLE_BUFFER      "SDL_VIDEO_DOUBLE_BUFFER"
```

## Remarks

By default, most lowlevel 2D APIs will use a triple buffer scheme that
wastes no CPU time on waiting for vsync after issuing a flip, but
introduces a frame of latency. On the other hand, using a double buffer
scheme instead is recommended for cases where low latency is an important
factor because we save a whole frame of latency. We do so by waiting for
vsync immediately after issuing a flip, usually just after eglSwapBuffers
call in the backend's *_SwapWindow function.

Since it's driver-specific, it's only supported where possible and
implemented. Currently supported the following drivers:

- KMSDRM (kmsdrm)
- Raspberry Pi (raspberrypi)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

