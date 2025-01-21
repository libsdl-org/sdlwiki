###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUViewport

A structure specifying a viewport.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUViewport
{
    float x;          /**< The left offset of the viewport. */
    float y;          /**< The top offset of the viewport. */
    float w;          /**< The width of the viewport. */
    float h;          /**< The height of the viewport. */
    float min_depth;  /**< The minimum depth of the viewport. */
    float max_depth;  /**< The maximum depth of the viewport. */
} SDL_GPUViewport;
```

## Version

This struct is available since SDL 3.2.0

## See Also

- [SDL_SetGPUViewport](SDL_SetGPUViewport)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

