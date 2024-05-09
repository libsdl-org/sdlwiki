###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_CreateWindow

Create a window with the specified position, dimensions, and flags.

## Header File

Defined in [SDL_video.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_video.h)

## Syntax

```c
SDL_Window * SDL_CreateWindow(const char *title,
                              int x, int y, int w,
                              int h, Uint32 flags);

```

## Function Parameters

|               |                                                                                                                                           |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| **title**     | the title of the window, in UTF-8 encoding                                                                                                |
| **x**         | the x position of the window, [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED), or [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED) |
| **y**         | the y position of the window, [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED), or [`SDL_WINDOWPOS_UNDEFINED`](SDL_WINDOWPOS_UNDEFINED) |
| **w**         | the width of the window, in screen coordinates                                                                                            |
| **h**         | the height of the window, in screen coordinates                                                                                           |
| **flags**     | 0, or one or more [SDL_WindowFlags](SDL_WindowFlags) OR'd together                                                                        |

## Return Value

Returns the [`SDL_Window`](SDL_Window) that was created or NULL on failure;
call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

`flags` may be any of the following OR'd together:

- [`SDL_WINDOW_FULLSCREEN`](SDL_WINDOW_FULLSCREEN): fullscreen window
- [`SDL_WINDOW_FULLSCREEN_DESKTOP`](SDL_WINDOW_FULLSCREEN_DESKTOP):
  fullscreen window at desktop resolution
- [`SDL_WINDOW_OPENGL`](SDL_WINDOW_OPENGL): window usable with an OpenGL
  context
- [`SDL_WINDOW_VULKAN`](SDL_WINDOW_VULKAN): window usable with a Vulkan
  instance
- [`SDL_WINDOW_METAL`](SDL_WINDOW_METAL): window usable with a Metal
  instance
- [`SDL_WINDOW_HIDDEN`](SDL_WINDOW_HIDDEN): window is not visible
- [`SDL_WINDOW_BORDERLESS`](SDL_WINDOW_BORDERLESS): no window decoration
- [`SDL_WINDOW_RESIZABLE`](SDL_WINDOW_RESIZABLE): window can be resized
- [`SDL_WINDOW_MINIMIZED`](SDL_WINDOW_MINIMIZED): window is minimized
- [`SDL_WINDOW_MAXIMIZED`](SDL_WINDOW_MAXIMIZED): window is maximized
- [`SDL_WINDOW_INPUT_GRABBED`](SDL_WINDOW_INPUT_GRABBED): window has
  grabbed input focus
- [`SDL_WINDOW_ALLOW_HIGHDPI`](SDL_WINDOW_ALLOW_HIGHDPI): window should be
  created in high-DPI mode if supported (>= SDL 2.0.1)

[`SDL_WINDOW_SHOWN`](SDL_WINDOW_SHOWN) is ignored by
[SDL_CreateWindow](SDL_CreateWindow)(). The [SDL_Window](SDL_Window) is
implicitly shown if [SDL_WINDOW_HIDDEN](SDL_WINDOW_HIDDEN) is not set.
[`SDL_WINDOW_SHOWN`](SDL_WINDOW_SHOWN) may be queried later using
[SDL_GetWindowFlags](SDL_GetWindowFlags)().

On Apple's macOS, you **must** set the NSHighResolutionCapable Info.plist
property to YES, otherwise you will not receive a High-DPI OpenGL canvas.

If the window is created with the
[`SDL_WINDOW_ALLOW_HIGHDPI`](SDL_WINDOW_ALLOW_HIGHDPI) flag, its size in
pixels may differ from its size in screen coordinates on platforms with
high-DPI support (e.g. iOS and macOS). Use
[SDL_GetWindowSize](SDL_GetWindowSize)() to query the client area's size in
screen coordinates, and [SDL_GL_GetDrawableSize](SDL_GL_GetDrawableSize)()
or [SDL_GetRendererOutputSize](SDL_GetRendererOutputSize)() to query the
drawable size in pixels. Note that when this flag is set, the drawable size
can vary after the window is created and should be queried after major
window events such as when the window is resized or moved between displays.

If the window is set fullscreen, the width and height parameters `w` and
`h` will not be used. However, invalid size parameters (e.g. too large) may
still fail. Window size is actually limited to 16384 x 16384 for all
platforms at window creation.

If the window is created with any of the
[SDL_WINDOW_OPENGL](SDL_WINDOW_OPENGL) or
[SDL_WINDOW_VULKAN](SDL_WINDOW_VULKAN) flags, then the corresponding
LoadLibrary function ([SDL_GL_LoadLibrary](SDL_GL_LoadLibrary) or
[SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary)) is called and the
corresponding UnloadLibrary function is called by
[SDL_DestroyWindow](SDL_DestroyWindow)().

If [SDL_WINDOW_VULKAN](SDL_WINDOW_VULKAN) is specified and there isn't a
working Vulkan driver, [SDL_CreateWindow](SDL_CreateWindow)() will fail
because [SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary)() will fail.

If [SDL_WINDOW_METAL](SDL_WINDOW_METAL) is specified on an OS that does not
support Metal, [SDL_CreateWindow](SDL_CreateWindow)() will fail.

On non-Apple devices, SDL requires you to either not link to the Vulkan
loader or link to a dynamic library version. This limitation may be removed
in a future version of SDL.

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CreateWindowFrom](SDL_CreateWindowFrom)
- [SDL_DestroyWindow](SDL_DestroyWindow)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVideo](CategoryVideo)


