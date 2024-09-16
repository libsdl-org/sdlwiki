###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GPUStoreOp

Specifies how the contents of a texture attached to a render pass are treated at the end of the render pass.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef enum SDL_GPUStoreOp
{
    SDL_GPU_STOREOP_STORE,             /**< The contents generated during the render pass will be written to memory. */
    SDL_GPU_STOREOP_DONT_CARE,         /**< The contents generated during the render pass are not needed and may be discarded. The contents will be undefined. */
    SDL_GPU_STOREOP_RESOLVE,           /**< The multisample contents generated during the render pass will be resolved to a non-multisample texture. The contents in the multisample texture may then be discarded and will be undefined. */
    SDL_GPU_STOREOP_RESOLVE_AND_STORE  /**< The multisample contents generated during the render pass will be resolved to a non-multisample texture. The contents in the multisample texture will be written to memory. */
} SDL_GPUStoreOp;
```

## Version

This enum is available since SDL 3.0.0

## See Also

- [SDL_BeginGPURenderPass](SDL_BeginGPURenderPass)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryGPU](CategoryGPU)

