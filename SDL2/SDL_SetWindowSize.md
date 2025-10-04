# SDL_SetWindowSize

Set the size of a window's client area.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_SetWindowSize(SDL_Window * window, int w,
                       int h);
```

## Function Parameters

|                            |            |                                                                         |
| -------------------------- | ---------- | ----------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window** | the window to change.                                                   |
| int                        | **w**      | the width of the window in pixels, in screen coordinates, must be > 0.  |
| int                        | **h**      | the height of the window in pixels, in screen coordinates, must be > 0. |

## Remarks

The window size in screen coordinates may differ from the size in pixels,
if the window was created with
[`SDL_WINDOW_ALLOW_HIGHDPI`](SDL_WINDOW_ALLOW_HIGHDPI) on a platform with
high-dpi support (e.g. iOS or macOS). Use
[SDL_GL_GetDrawableSize](SDL_GL_GetDrawableSize)() or
[SDL_GetRendererOutputSize](SDL_GetRendererOutputSize)() to get the real
client area size in pixels.

Fullscreen windows automatically match the size of the display mode, and
you should use [SDL_SetWindowDisplayMode](SDL_SetWindowDisplayMode)() to
change their size.

## Thread Safety

This function should only be called on the main thread.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GetWindowSize](SDL_GetWindowSize)
- [SDL_SetWindowDisplayMode](SDL_SetWindowDisplayMode)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)

