# SDL_HINT_VIDEO_X11_ENABLE_XSYNC_EXT

A variable controlling whether the X Synchronization Extension is enabled.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VIDEO_X11_ENABLE_XSYNC_EXT "SDL_VIDEO_X11_ENABLE_XSYNC_EXT"
```

## Remarks

If set, this can result in smoother window resizing when rendering using
OpenGL, however, there are some conditions:

- It is only activated on windows created with the
  [`SDL_WINDOW_OPENGL`](SDL_WINDOW_OPENGL) flag (windows using an SDL
  OpenGL renderer have this automatically set).
- When activated, presentation must be done with `SDL_GL_SwapWindow()`
  (`SDL_RenderPresent()` calls this internally for OpenGL renderers as
  well).

Enabling this and presenting via an external mechanism will result in sync
requests not being acked, and hangs and other odd window behavior may
result.

The variable can be set to the following values:

- "0": The X Synchronization Extension is disabled. (default)
- "1": The X Synchronization Extension is enabled.

This hint should be set before creating a window.

## Version

This hint is available since SDL 3.4.10.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

