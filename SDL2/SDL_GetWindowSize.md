###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetWindowSize

Get the size of a window's client area.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
void SDL_GetWindowSize(SDL_Window * window, int *w,
                       int *h);

```

## Function Parameters

|                |                                                                                       |
| -------------- | ------------------------------------------------------------------------------------- |
| **window**     | the window to query the width and height from                                         |
| **w**          | a pointer filled in with the width of the window, in screen coordinates, may be NULL  |
| **h**          | a pointer filled in with the height of the window, in screen coordinates, may be NULL |

## Remarks

NULL can safely be passed as the `w` or `h` parameter if the width or
height value is not desired.

The window size in screen coordinates may differ from the size in pixels,
if the window was created with
[`SDL_WINDOW_ALLOW_HIGHDPI`](SDL_WINDOW_ALLOW_HIGHDPI) on a platform with
high-dpi support (e.g. iOS or macOS). Use
[SDL_GL_GetDrawableSize](SDL_GL_GetDrawableSize)(),
[SDL_Vulkan_GetDrawableSize](SDL_Vulkan_GetDrawableSize)(), or
[SDL_GetRendererOutputSize](SDL_GetRendererOutputSize)() to get the real
client area size in pixels.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_GL_GetDrawableSize](SDL_GL_GetDrawableSize)
- [SDL_Vulkan_GetDrawableSize](SDL_Vulkan_GetDrawableSize)
- [SDL_SetWindowSize](SDL_SetWindowSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

