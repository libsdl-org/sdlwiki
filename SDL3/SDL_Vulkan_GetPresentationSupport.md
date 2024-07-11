###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Vulkan_GetPresentationSupport

Query support for presentation via a given physical device and queue family.

## Header File

Defined in [<SDL3/SDL_vulkan.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_vulkan.h)

## Syntax

```c
SDL_bool SDL_Vulkan_GetPresentationSupport(VkInstance instance,
                                           VkPhysicalDevice physicalDevice,
                                           Uint32 queueFamilyIndex);
```

## Function Parameters

|                  |                      |                                                           |
| ---------------- | -------------------- | --------------------------------------------------------- |
| VkInstance       | **instance**         | the Vulkan instance handle.                               |
| VkPhysicalDevice | **physicalDevice**   | a valid Vulkan physical device handle.                    |
| Uint32           | **queueFamilyIndex** | a valid queue family index for the given physical device. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if supported,
[SDL_FALSE](SDL_FALSE) if unsupported or an error occurred.

## Remarks

The `instance` must have been created with extensions returned by
[SDL_Vulkan_GetInstanceExtensions](SDL_Vulkan_GetInstanceExtensions)()
enabled.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_Vulkan_GetInstanceExtensions](SDL_Vulkan_GetInstanceExtensions)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVulkan](CategoryVulkan)

