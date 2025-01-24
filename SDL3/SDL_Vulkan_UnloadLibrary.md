# SDL_Vulkan_UnloadLibrary

Unload the Vulkan library previously loaded by [SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary)().

## Header File

Defined in [<SDL3/SDL_vulkan.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_vulkan.h)

## Syntax

```c
void SDL_Vulkan_UnloadLibrary(void);
```

## Remarks

SDL keeps a counter of how many times this function has been called, so it
is safe to call this function multiple times, so long as it is paired with
an equivalent number of calls to
[SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary). The library isn't
actually unloaded until there have been an equivalent number of calls to
[SDL_Vulkan_UnloadLibrary](SDL_Vulkan_UnloadLibrary).

Once the library has actually been unloaded, if any Vulkan instances
remain, they will likely crash the program. Clean up any existing Vulkan
resources, and destroy appropriate windows, renderers and GPU devices
before calling this function.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryVulkan](CategoryVulkan)

