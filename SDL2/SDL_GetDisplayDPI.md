###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GetDisplayDPI

Get the dots/pixels-per-inch for a display.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
int SDL_GetDisplayDPI(int displayIndex, float * ddpi, float * hdpi, float * vdpi);

```

## Function Parameters

|                      |                                                                         |
| -------------------- | ----------------------------------------------------------------------- |
| **displayIndex**     | the index of the display from which DPI information should be queried   |
| **ddpi**             | a pointer filled in with the diagonal DPI of the display; may be NULL   |
| **hdpi**             | a pointer filled in with the horizontal DPI of the display; may be NULL |
| **vdpi**             | a pointer filled in with the vertical DPI of the display; may be NULL   |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Diagonal, horizontal and vertical DPI can all be optionally returned if the
appropriate parameter is non-NULL.

A failure of this function usually means that either no DPI information is
available or the `displayIndex` is out of range.

**WARNING**: This reports the DPI that the hardware reports, and it is not
always reliable! It is almost always better to use
[SDL_GetWindowSize](SDL_GetWindowSize)() to find the window size, which
might be in logical points instead of pixels, and then
[SDL_GL_GetDrawableSize](SDL_GL_GetDrawableSize)(),
[SDL_Vulkan_GetDrawableSize](SDL_Vulkan_GetDrawableSize)(),
[SDL_Metal_GetDrawableSize](SDL_Metal_GetDrawableSize)(), or
[SDL_GetRendererOutputSize](SDL_GetRendererOutputSize)(), and compare the
two values to get an actual scaling value between the two. We will be
rethinking how high-dpi details should be managed in SDL3 to make things
more consistent, reliable, and clear.

## Version

This function is available since SDL 2.0.4.

## See Also

- [SDL_GetNumVideoDisplays](SDL_GetNumVideoDisplays)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

