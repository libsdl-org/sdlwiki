# SDL_GPUIndirectDispatchCommand

A structure specifying the parameters of an indexed dispatch command.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUIndirectDispatchCommand
{
    Uint32 groupcount_x;  /**< The number of local workgroups to dispatch in the X dimension. */
    Uint32 groupcount_y;  /**< The number of local workgroups to dispatch in the Y dimension. */
    Uint32 groupcount_z;  /**< The number of local workgroups to dispatch in the Z dimension. */
} SDL_GPUIndirectDispatchCommand;
```

## Version

This struct is available since SDL 3.2.0.

## See Also

- [SDL_DispatchGPUComputeIndirect](SDL_DispatchGPUComputeIndirect)






----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

