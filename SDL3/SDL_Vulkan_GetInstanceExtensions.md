###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Vulkan_GetInstanceExtensions

Get the Vulkan instance extensions needed for vkCreateInstance.

## Syntax

```c
char const* const* SDL_Vulkan_GetInstanceExtensions(Uint32 *pCount);

```

## Function Parameters

|                |                                                                                 |
| -------------- | ------------------------------------------------------------------------------- |
| **pCount**     | A pointer to Uint32 that will be filled with the number of extensions returned. |

## Return Value

Returns An array of extension name strings on success, NULL on error.

## Remarks

This should be called after either calling
[SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary.md)() or creating an
[SDL_Window](SDL_Window.md) with the [`SDL_WINDOW_VULKAN`](SDL_WINDOW_VULKAN)
flag.

On return, the variable pointed to by `pCount` will be set to the number of
elements returned, suitable for using with
VkInstanceCreateInfo::enabledExtensionCount, and the returned array can be
used with VkInstanceCreateInfo::ppEnabledExtensionNames, for calling
Vulkan's vkCreateInstance API.

You should not free the returned array; it is owned by SDL.

## Version

This function is available since SDL 3.0.0.

## Code Examples

```c++
// Note: This sample uses C++17 features/syntax.
// Get the required extension count
unsigned int count;
if (!SDL_Vulkan_GetInstanceExtensions(window, &count, nullptr)) handle_error();

std::vector<const char*> extensions = {
    VK_EXT_DEBUG_REPORT_EXTENSION_NAME // Sample additional extension
};
size_t additional_extension_count = extensions.size();
extensions.resize(additional_extension_count + count);

if (!SDL_Vulkan_GetInstanceExtensions(window, &count, extensions.data() + additional_extension_count)) handle_error();

// Now we can make the Vulkan instance
VkInstanceCreateInfo create_info = {};
create_info.enabledExtensionCount = static_cast<uint32_t>(extensions.size());
create_info.ppEnabledExtensionNames = extensions.data();

VkInstance instance;
VkResult result = vkCreateInstance(&create_info, nullptr, &instance);
```

## Related Functions

* [SDL_Vulkan_CreateSurface](SDL_Vulkan_CreateSurface.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryVulkan](CategoryVulkan.md)
