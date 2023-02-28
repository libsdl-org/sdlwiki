###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Vulkan_GetVkGetInstanceProcAddr

Get the address of the `vkGetInstanceProcAddr` function.

## Syntax

```c
SDL_FunctionPointer SDL_Vulkan_GetVkGetInstanceProcAddr(void);

```

## Return Value

Returns the function pointer for `vkGetInstanceProcAddr` or NULL on error.

## Remarks

This should be called after either calling
[SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary)() or creating an
[SDL_Window](SDL_Window) with the [`SDL_WINDOW_VULKAN`](SDL_WINDOW_VULKAN)
flag.

The actual type of the returned function pointer is
PFN_vkGetInstanceProcAddr, but that isn't available because the Vulkan
headers are not included here. You should cast the return value of this
function to that type, e.g.

`vkGetInstanceProcAddr =
(PFN_vkGetInstanceProcAddr)SDL_Vulkan_GetVkGetInstanceProcAddr();`

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI)

