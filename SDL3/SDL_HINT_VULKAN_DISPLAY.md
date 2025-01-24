# SDL_HINT_VULKAN_DISPLAY

A variable overriding the display index used in [SDL_Vulkan_CreateSurface](SDL_Vulkan_CreateSurface)()

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_VULKAN_DISPLAY "SDL_VULKAN_DISPLAY"
```

## Remarks

The display index starts at 0, which is the default.

This hint should be set before calling
[SDL_Vulkan_CreateSurface](SDL_Vulkan_CreateSurface)()

## Version

This hint is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

