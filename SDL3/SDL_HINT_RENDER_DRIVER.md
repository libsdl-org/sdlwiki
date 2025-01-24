# SDL_HINT_RENDER_DRIVER

A variable specifying which render driver to use.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_DRIVER "SDL_RENDER_DRIVER"
```

## Remarks

If the application doesn't pick a specific renderer to use, this variable
specifies the name of the preferred renderer. If the preferred renderer
can't be initialized, creating a renderer will fail.

This variable is case insensitive and can be set to the following values:

- "direct3d"
- "direct3d11"
- "direct3d12"
- "opengl"
- "opengles2"
- "opengles"
- "metal"
- "vulkan"
- "gpu"
- "software"

This hint accepts a comma-separated list of driver names, and each will be
tried in the order listed when creating a renderer until one succeeds or
all of them fail.

The default varies by platform, but it's the first one in the list that is
available on the current platform.

This hint should be set before creating a renderer.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

