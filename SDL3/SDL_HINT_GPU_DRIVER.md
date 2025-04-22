# SDL_HINT_GPU_DRIVER

A variable that specifies a GPU backend to use.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_GPU_DRIVER "SDL_GPU_DRIVER"
```

## Remarks

By default, SDL will try all available GPU backends in a reasonable order
until it finds one that can work, but this hint allows the app or user to
force a specific target, such as "direct3d12" if, say, your hardware
supports Vulkan but you want to try using D3D12 instead.

This hint should be set before any GPU functions are called.

## Version

This hint is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

