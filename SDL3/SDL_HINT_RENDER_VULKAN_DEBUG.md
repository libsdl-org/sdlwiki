###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_RENDER_VULKAN_DEBUG

A variable controlling whether to enable Vulkan Validation Layers.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_RENDER_VULKAN_DEBUG    "SDL_RENDER_VULKAN_DEBUG"
```

## Remarks

This variable can be set to the following values:

- "0": Disable Validation Layer use
- "1": Enable Validation Layer use

By default, SDL does not use Vulkan Validation Layers.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

