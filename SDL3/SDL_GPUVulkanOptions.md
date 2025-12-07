# SDL_GPUVulkanOptions

A structure specifying additional options when using Vulkan.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUVulkanOptions
{
    Uint32 vulkan_api_version; /**< The Vulkan API version to request for the instance. Use Vulkan's VK_MAKE_VERSION or VK_MAKE_API_VERSION. */
    void *feature_list; /**< Pointer to the first element of a chain of Vulkan feature structs. (Requires API version 1.1 or higher.)*/
	void *vulkan_10_physical_device_features; /**< Pointer to a VkPhysicalDeviceFeatures struct to enable additional Vulkan 1.0 features. */
	Uint32 device_extension_count; /**< Number of additional device extensions to require. */
	const char **device_extension_names; /**< Pointer to a list of additional device extensions to require. */
	Uint32 instance_extension_count; /**< Number of additional instance extensions to require. */
	const char **instance_extension_names; /**< Pointer to a list of additional instance extensions to require. */
} SDL_GPUVulkanOptions;
```

## Remarks

When no such structure is provided, SDL will use Vulkan API version 1.0 and
a minimal set of features. The requested API version influences how the
feature_list is processed by SDL. When requesting API version 1.0, the
feature_list is ignored. Only the vulkan_10_physical_device_features and
the extension lists are used. When requesting API version 1.1, the
feature_list is scanned for feature structures introduced in Vulkan 1.1.
When requesting Vulkan 1.2 or higher, the feature_list is additionally
scanned for compound feature structs such as
VkPhysicalDeviceVulkan11Features. The device and instance extension lists,
as well as vulkan_10_physical_device_features, are always processed.

## Version

This struct is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

