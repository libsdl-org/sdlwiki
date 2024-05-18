###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Vulkan_DestroySurface

Destroy the Vulkan rendering surface of a window.

## Header File

Defined in [<SDL3/SDL_vulkan.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_vulkan.h)

## Syntax

```c
void SDL_Vulkan_DestroySurface(VkInstance instance,
                           VkSurfaceKHR surface,
                           const struct VkAllocationCallbacks *allocator);

```

## Function Parameters

|                   |                                                                                                              |
| ----------------- | ------------------------------------------------------------------------------------------------------------ |
| **instance**      | The Vulkan instance handle                                                                                   |
| **surface**       | VkSurfaceKHR handle to destroy                                                                               |
| **allocator**     | A VkAllocationCallbacks struct, which lets the app set the allocator that destroys the surface. Can be NULL. |

## Remarks

This should be called before [SDL_DestroyWindow](SDL_DestroyWindow), if
[SDL_Vulkan_CreateSurface](SDL_Vulkan_CreateSurface) was called after
[SDL_CreateWindow](SDL_CreateWindow).

The `instance` must have been created with extensions returned by
[SDL_Vulkan_GetInstanceExtensions](SDL_Vulkan_GetInstanceExtensions)()
enabled and `surface` must have been created successfully by an
[SDL_Vulkan_CreateSurface](SDL_Vulkan_CreateSurface)() call.

If `allocator` is NULL, Vulkan will use the system default allocator. This
argument is passed directly to Vulkan and isn't used by SDL itself.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_Vulkan_GetInstanceExtensions](SDL_Vulkan_GetInstanceExtensions)
- [SDL_Vulkan_CreateSurface](SDL_Vulkan_CreateSurface)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVulkan](CategoryVulkan)

