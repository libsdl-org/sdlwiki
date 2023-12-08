###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Vulkan_CreateSurface

Create a Vulkan rendering surface for a window.

## Syntax

```c
SDL_bool SDL_Vulkan_CreateSurface(SDL_Window *window,
                                  VkInstance instance,
                                  const struct VkAllocationCallbacks *allocator,
                                  VkSurfaceKHR* surface);

```

## Function Parameters

|                   |                                                                                                             |
| ----------------- | ----------------------------------------------------------------------------------------------------------- |
| **window**        | The window to which to attach the Vulkan surface                                                            |
| **instance**      | The Vulkan instance handle                                                                                  |
| **allocator**     | A VkAllocationCallbacks struct, which lets the app set the allocator that creates the surface. Can be NULL. |
| **surface**       | A pointer to a VkSurfaceKHR handle to output the newly created surface                                      |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) on success, [SDL_FALSE](SDL_FALSE.md) on error.

## Remarks

The `window` must have been created with the
[`SDL_WINDOW_VULKAN`](SDL_WINDOW_VULKAN) flag and `instance` must have been
created with extensions returned by
[SDL_Vulkan_GetInstanceExtensions](SDL_Vulkan_GetInstanceExtensions.md)()
enabled.

If `allocator` is NULL, Vulkan will use the system default allocator. This
argument is passed directly to Vulkan and isn't used by SDL itself.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
VkSurfaceKHR surface;

if (!SDL_Vulkan_CreateSurface(window, instance, &surface)) handle_error();
```

## Related Functions

* [SDL_Vulkan_GetInstanceExtensions](SDL_Vulkan_GetInstanceExtensions.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVulkan](CategoryVulkan.md)
<!-- #See the Style Guide for instructions on editing the footer. -->
