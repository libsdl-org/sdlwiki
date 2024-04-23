###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_VIDEO_DOUBLE_BUFFER

Tell the video driver that we only want a double buffer.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_DOUBLE_BUFFER      "SDL_VIDEO_DOUBLE_BUFFER"
```

## Remarks

By default, most lowlevel 2D APIs will use a triple buffer scheme that
wastes no CPU time on waiting for vsync after issuing a flip, but
introduces a frame of latency. On the other hand, using a double buffer
scheme instead is recommended for cases where low latency is an important
factor because we save a whole frame of latency.

We do so by waiting for vsync immediately after issuing a flip, usually
just after eglSwapBuffers call in the backend's *_SwapWindow function.

This hint is currently supported on the following drivers:

- Raspberry Pi (raspberrypi)

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

