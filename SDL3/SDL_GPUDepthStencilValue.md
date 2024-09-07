###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUDepthStencilValue

A structure specifying a depth-stencil clear value.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUDepthStencilValue
{
    float depth;    /**< The clear value for the depth aspect of the depth-stencil target. */
    Uint8 stencil;  /**< The clear value for the stencil aspect of the depth-stencil target. */
    Uint8 padding1;
    Uint8 padding2;
    Uint8 padding3;
} SDL_GPUDepthStencilValue;
```

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_GPUDepthStencilTargetInfo](SDL_GPUDepthStencilTargetInfo)
- [SDL_BeginGPURenderPass](SDL_BeginGPURenderPass)

----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

