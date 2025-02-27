# SDL_GPUBufferUsageFlags

Specifies how a buffer is intended to be used by the client.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
typedef Uint32 SDL_GPUBufferUsageFlags;

#define SDL_GPU_BUFFERUSAGE_VERTEX                                  (1u << 0) /**< Buffer is a vertex buffer. */
#define SDL_GPU_BUFFERUSAGE_INDEX                                   (1u << 1) /**< Buffer is an index buffer. */
#define SDL_GPU_BUFFERUSAGE_INDIRECT                                (1u << 2) /**< Buffer is an indirect buffer. */
#define SDL_GPU_BUFFERUSAGE_GRAPHICS_STORAGE_READ                   (1u << 3) /**< Buffer supports storage reads in graphics stages. */
#define SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_READ                    (1u << 4) /**< Buffer supports storage reads in the compute stage. */
#define SDL_GPU_BUFFERUSAGE_COMPUTE_STORAGE_WRITE                   (1u << 5) /**< Buffer supports storage writes in the compute stage. */
```

## Remarks

A buffer must have at least one usage flag. Note that some usage flag
combinations are invalid.

Unlike textures, READ | WRITE can be used for simultaneous read-write
usage. The same data synchronization concerns as textures apply.

If you use a STORAGE flag, the data in the buffer must respect std140
layout conventions. In practical terms this means you must ensure that vec3
and vec4 fields are 16-byte aligned.

## Version

This datatype is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUBuffer](SDL_CreateGPUBuffer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIDatatype](CategoryAPIDatatype), [CategoryGPU](CategoryGPU)

