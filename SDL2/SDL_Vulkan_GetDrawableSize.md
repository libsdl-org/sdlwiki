###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Vulkan_GetDrawableSize

Get the size of the window's underlying drawable dimensions in pixels.

## Header File

Defined in [SDL_vulkan.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_vulkan.h)

## Syntax

```c
void SDL_Vulkan_GetDrawableSize(SDL_Window * window,
                                int *w, int *h);

```

## Function Parameters

|                |                                                                 |
| -------------- | --------------------------------------------------------------- |
| **window**     | an [SDL_Window](SDL_Window) for which the size is to be queried |
| **w**          | Pointer to the variable to write the width to or NULL           |
| **h**          | Pointer to the variable to write the height to or NULL          |

## Remarks

This may differ from [SDL_GetWindowSize](SDL_GetWindowSize)() if we're
rendering to a high-DPI drawable, i.e. the window was created with
[`SDL_WINDOW_ALLOW_HIGHDPI`](SDL_WINDOW_ALLOW_HIGHDPI) on a platform with
high-DPI support (Apple calls this "Retina"), and not disabled by the
[`SDL_HINT_VIDEO_HIGHDPI_DISABLED`](SDL_HINT_VIDEO_HIGHDPI_DISABLED) hint.

## Version

This function is available since SDL 2.0.6.

## See Also

- [SDL_GetWindowSize](SDL_GetWindowSize)
- [SDL_CreateWindow](SDL_CreateWindow)
- [SDL_Vulkan_CreateSurface](SDL_Vulkan_CreateSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVulkan](CategoryVulkan)

