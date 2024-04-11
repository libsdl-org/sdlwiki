###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_VIDEO_FOREIGN_WINDOW_VULKAN

When calling [SDL_CreateWindowFrom](SDL_CreateWindowFrom)(), make the window compatible with Vulkan.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_VIDEO_FOREIGN_WINDOW_VULKAN "SDL_VIDEO_FOREIGN_WINDOW_VULKAN"
```

## Remarks

This variable can be set to the following values: "0" - Don't add any
graphics flags to the [SDL_WindowFlags](SDL_WindowFlags) "1" - Add
[SDL_WINDOW_VULKAN](SDL_WINDOW_VULKAN) to the
[SDL_WindowFlags](SDL_WindowFlags)

By default SDL will not make the foreign window compatible with Vulkan.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

