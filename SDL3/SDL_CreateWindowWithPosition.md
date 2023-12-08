###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateWindowWithPosition

Create a window with the specified position, dimensions, and flags.

## Syntax

```c
SDL_Window* SDL_CreateWindowWithPosition(const char *title, int x, int y, int w, int h, Uint32 flags);

```

## Function Parameters

|               |                                                                                     |
| ------------- | ----------------------------------------------------------------------------------- |
| **title**     | the title of the window, in UTF-8 encoding                                          |
| **x**         | the x position of the window, or [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED) |
| **y**         | the y position of the window, or [`SDL_WINDOWPOS_CENTERED`](SDL_WINDOWPOS_CENTERED) |
| **w**         | the width of the window                                                             |
| **h**         | the height of the window                                                            |
| **flags**     | 0, or one or more [SDL_WindowFlags](SDL_WindowFlags.md) OR'd together                  |

## Return Value

Returns the window that was created or NULL on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

`flags` may be any of the following OR'd together:

- [`SDL_WINDOW_FULLSCREEN`](SDL_WINDOW_FULLSCREEN): fullscreen window at
  desktop resolution
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
- [`SDL_WINDOW_MOUSE_GRABBED`](SDL_WINDOW_MOUSE_GRABBED): window has
  grabbed mouse focus

The [SDL_Window](SDL_Window.md) is implicitly shown if
[SDL_WINDOW_HIDDEN](SDL_WINDOW_HIDDEN.md) is not set.

On Apple's macOS, you **must** set the NSHighResolutionCapable Info.plist
property to YES, otherwise you will not receive a High-DPI OpenGL canvas.

The window pixel size may differ from its window coordinate size if the
window is on a high pixel density display. Use
[SDL_GetWindowSize](SDL_GetWindowSize.md)() to query the client area's size in
window coordinates, and
[SDL_GetWindowSizeInPixels](SDL_GetWindowSizeInPixels.md)() or
[SDL_GetRenderOutputSize](SDL_GetRenderOutputSize.md)() to query the drawable
size in pixels. Note that the drawable size can vary after the window is
created and should be queried again if you get an
[SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED](SDL_EVENT_WINDOW_PIXEL_SIZE_CHANGED.md)
event.

If the window is set fullscreen, the width and height parameters `w` and
`h` will not be used. However, invalid size parameters (e.g. too large) may
still fail. Window size is actually limited to 16384 x 16384 for all
platforms at window creation.

If the window is created with any of the
[SDL_WINDOW_OPENGL](SDL_WINDOW_OPENGL.md) or
[SDL_WINDOW_VULKAN](SDL_WINDOW_VULKAN.md) flags, then the corresponding
LoadLibrary function ([SDL_GL_LoadLibrary](SDL_GL_LoadLibrary.md) or
[SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary.md)) is called and the
corresponding UnloadLibrary function is called by
[SDL_DestroyWindow](SDL_DestroyWindow.md)().

If [SDL_WINDOW_VULKAN](SDL_WINDOW_VULKAN.md) is specified and there isn't a
working Vulkan driver, [SDL_CreateWindow](SDL_CreateWindow.md)() will fail
because [SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary.md)() will fail.

If [SDL_WINDOW_METAL](SDL_WINDOW_METAL.md) is specified on an OS that does not
support Metal, [SDL_CreateWindow](SDL_CreateWindow.md)() will fail.

On non-Apple devices, SDL requires you to either not link to the Vulkan
loader or link to a dynamic library version. This limitation may be removed
in a future version of SDL.

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_CreatePopupWindow](SDL_CreatePopupWindow.md)
* [SDL_CreateWindow](SDL_CreateWindow.md)
* [SDL_CreateWindowFrom](SDL_CreateWindowFrom.md)
* [SDL_DestroyWindow](SDL_DestroyWindow.md)

----
[CategoryAPI](CategoryAPI.md)
