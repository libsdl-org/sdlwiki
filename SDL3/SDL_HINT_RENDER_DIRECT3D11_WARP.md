# SDL_HINT_RENDER_DIRECT3D11_WARP

A variable controlling whether to use the Direct3D 11 WARP software rasterizer.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_RENDER_DIRECT3D11_WARP "SDL_RENDER_DIRECT3D11_WARP"
```

## Remarks

For more information, see:
https://learn.microsoft.com/en-us/windows/win32/direct3darticles/directx-warp

The variable can be set to the following values:

- "0": Disable WARP rasterizer. (default)
- "1": Enable WARP rasterizer.

This hint should be set before creating a renderer.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

