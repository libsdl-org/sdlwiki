# SDL_HINT_RENDER_VULKAN_DEBUG

A variable controlling whether to enable Vulkan Validation Layers.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_VULKAN_DEBUG "SDL_RENDER_VULKAN_DEBUG"
```

## Remarks

This variable can be set to the following values:

- "0": Disable Validation Layer use
- "1": Enable Validation Layer use

By default, SDL does not use Vulkan Validation Layers.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

