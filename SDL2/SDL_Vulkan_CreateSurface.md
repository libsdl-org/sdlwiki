###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Vulkan_CreateSurface

Create a Vulkan rendering surface for a window.

## Header File

Defined in [SDL_vulkan.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_vulkan.h)

## Syntax

```c
SDL_bool SDL_Vulkan_CreateSurface(SDL_Window *window,
                              VkInstance instance,
                              VkSurfaceKHR* surface);
```

## Function Parameters

|                            |              |                                                                         |
| -------------------------- | ------------ | ----------------------------------------------------------------------- |
| [SDL_Window](SDL_Window) * | **window**   | The window to which to attach the Vulkan surface.                       |
| VkInstance                 | **instance** | The Vulkan instance handle.                                             |
| VkSurfaceKHR *             | **surface**  | A pointer to a VkSurfaceKHR handle to output the newly created surface. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success,
[SDL_FALSE](SDL_FALSE) on error.

## Remarks

The `window` must have been created with the
[`SDL_WINDOW_VULKAN`](SDL_WINDOW_VULKAN) flag and `instance` must have been
created with extensions returned by
[SDL_Vulkan_GetInstanceExtensions](SDL_Vulkan_GetInstanceExtensions)()
enabled.

## Version

This function is available since SDL 2.0.6.

## See Also

- [SDL_Vulkan_GetInstanceExtensions](SDL_Vulkan_GetInstanceExtensions)
- [SDL_Vulkan_GetDrawableSize](SDL_Vulkan_GetDrawableSize)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVulkan](CategoryVulkan)

