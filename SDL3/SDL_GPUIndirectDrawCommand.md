###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GPUIndirectDrawCommand

A structure specifying the parameters of an indirect draw command.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef struct SDL_GPUIndirectDrawCommand
{
    Uint32 num_vertices;   /**< The number of vertices to draw. */
    Uint32 num_instances;  /**< The number of instances to draw. */
    Uint32 first_vertex;   /**< The index of the first vertex to draw. */
    Uint32 first_instance; /**< The ID of the first instance to draw. */
} SDL_GPUIndirectDrawCommand;
```

## Remarks

Note that the `first_vertex` and `first_instance` parameters are NOT
compatible with built-in vertex/instance ID variables in shaders (for
example, SV_VertexID). If your shader depends on these variables, the
correlating draw call parameter MUST be 0.

## Version

This struct is available since SDL 3.0.0

## See Also

- [SDL_DrawGPUPrimitivesIndirect](SDL_DrawGPUPrimitivesIndirect)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIStruct](CategoryAPIStruct), [CategoryGPU](CategoryGPU)

