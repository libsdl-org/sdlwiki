###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_Vulkan_GetVkGetInstanceProcAddr

Get the address of the `vkGetInstanceProcAddr` function.

## Header File

Defined in [SDL_vulkan.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_vulkan.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
void* SDL_Vulkan_GetVkGetInstanceProcAddr(void);

```

## Return Value

Returns the function pointer for `vkGetInstanceProcAddr` or NULL on error.

## Remarks

This should be called after either calling
[SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary)() or creating an
[SDL_Window](SDL_Window) with the [`SDL_WINDOW_VULKAN`](SDL_WINDOW_VULKAN)
flag.

## Version

This function is available since SDL 2.0.6.

----
[CategoryAPI](CategoryAPI)

