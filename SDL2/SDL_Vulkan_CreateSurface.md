###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Vulkan_CreateSurface

Create a Vulkan rendering surface for a window.

## Syntax

```c
SDL_bool SDL_Vulkan_CreateSurface(SDL_Window *window,
                                  VkInstance instance,
                                  VkSurfaceKHR* surface);

```

## Function Parameters

|                  |                                                                        |
| ---------------- | ---------------------------------------------------------------------- |
| **window**       | The window to which to attach the Vulkan surface                       |
| **instance**     | The Vulkan instance handle                                             |
| **surface**      | A pointer to a VkSurfaceKHR handle to output the newly created surface |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) on success, [SDL_FALSE](SDL_FALSE.md) on error.

## Remarks

The `window` must have been created with the
[`SDL_WINDOW_VULKAN`](SDL_WINDOW_VULKAN) flag and `instance` must have been
created with extensions returned by
[SDL_Vulkan_GetInstanceExtensions](SDL_Vulkan_GetInstanceExtensions.md)()
enabled.

## Version

This function is available since SDL 2.0.6.

## Related Functions

* [SDL_Vulkan_GetInstanceExtensions](SDL_Vulkan_GetInstanceExtensions.md)
* [SDL_Vulkan_GetDrawableSize](SDL_Vulkan_GetDrawableSize.md)

----
[CategoryAPI](CategoryAPI.md)
