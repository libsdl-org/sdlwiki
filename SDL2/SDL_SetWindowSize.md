###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetWindowSize

Set the size of a window's client area.

## Syntax

```c
void SDL_SetWindowSize(SDL_Window * window, int w,
                       int h);

```

## Function Parameters

|                |                                                                        |
| -------------- | ---------------------------------------------------------------------- |
| **window**     | the window to change                                                   |
| **w**          | the width of the window in pixels, in screen coordinates, must be > 0  |
| **h**          | the height of the window in pixels, in screen coordinates, must be > 0 |

## Remarks

The window size in screen coordinates may differ from the size in pixels,
if the window was created with
[`SDL_WINDOW_ALLOW_HIGHDPI`](SDL_WINDOW_ALLOW_HIGHDPI) on a platform with
high-dpi support (e.g. iOS or macOS). Use
[SDL_GL_GetDrawableSize](SDL_GL_GetDrawableSize.md)() or
[SDL_GetRendererOutputSize](SDL_GetRendererOutputSize.md)() to get the real
client area size in pixels.

Fullscreen windows automatically match the size of the display mode, and
you should use [SDL_SetWindowDisplayMode](SDL_SetWindowDisplayMode.md)() to
change their size.

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_GetWindowSize](SDL_GetWindowSize.md)
* [SDL_SetWindowDisplayMode](SDL_SetWindowDisplayMode.md)

----
[CategoryAPI](CategoryAPI.md)
