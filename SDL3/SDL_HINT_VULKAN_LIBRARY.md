###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_VULKAN_LIBRARY

Specify the Vulkan library to load.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VULKAN_LIBRARY "SDL_VULKAN_LIBRARY"
```

## Remarks

This hint should be set before creating a Vulkan window or calling
[SDL_Vulkan_LoadLibrary](SDL_Vulkan_LoadLibrary)().

## Version

This hint is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

