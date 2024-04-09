###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_RENDER_DRIVER

A variable specifying which render driver to use.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_RENDER_DRIVER              "SDL_RENDER_DRIVER"
```

## Remarks

If the application doesn't pick a specific renderer to use, this variable
specifies the name of the preferred renderer. If the preferred renderer
can't be initialized, the normal default renderer is used.

This variable is case insensitive and can be set to the following values:

- "direct3d"
- "direct3d11"
- "direct3d12"
- "opengl"
- "opengles2"
- "opengles"
- "metal"
- "vulkan"
- "software"

The default varies by platform, but it's the first one in the list that is
available on the current platform.

This hint should be set before creating a renderer.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [[CategoryDefine]], [[CategoryHints]]


