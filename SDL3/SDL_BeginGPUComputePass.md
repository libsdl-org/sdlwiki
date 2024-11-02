###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BeginGPUComputePass

Begins a compute pass on a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUComputePass* SDL_BeginGPUComputePass(
    SDL_GPUCommandBuffer *command_buffer,
    const SDL_GPUStorageTextureReadWriteBinding *storage_texture_bindings,
    Uint32 num_storage_texture_bindings,
    const SDL_GPUStorageBufferReadWriteBinding *storage_buffer_bindings,
    Uint32 num_storage_buffer_bindings);
```

## Function Parameters

|                                                                                        |                                  |                                                        |
| -------------------------------------------------------------------------------------- | -------------------------------- | ------------------------------------------------------ |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) *                                         | **command_buffer**               | a command buffer.                                      |
| const [SDL_GPUStorageTextureReadWriteBinding](SDL_GPUStorageTextureReadWriteBinding) * | **storage_texture_bindings**     | an array of writeable storage texture binding structs. |
| [Uint32](Uint32)                                                                       | **num_storage_texture_bindings** | the number of storage textures to bind from the array. |
| const [SDL_GPUStorageBufferReadWriteBinding](SDL_GPUStorageBufferReadWriteBinding) *   | **storage_buffer_bindings**      | an array of writeable storage buffer binding structs.  |
| [Uint32](Uint32)                                                                       | **num_storage_buffer_bindings**  | the number of storage buffers to bind from the array.  |

## Return Value

([SDL_GPUComputePass](SDL_GPUComputePass) *) Returns a compute pass handle.

## Remarks

A compute pass is defined by a set of texture subresources and buffers that
may be written to by compute pipelines. These textures and buffers must
have been created with the COMPUTE_STORAGE_WRITE bit or the
COMPUTE_STORAGE_SIMULTANEOUS_READ_WRITE bit. If you do not create a texture
with COMPUTE_STORAGE_SIMULTANEOUS_READ_WRITE, you must not read from the
texture in the compute pass. All operations related to compute pipelines
must take place inside of a compute pass. You must not begin another
compute pass, or a render pass or copy pass before ending the compute pass.

A VERY IMPORTANT NOTE - Reads and writes in compute passes are NOT
implicitly synchronized. This means you may cause data races by both
reading and writing a resource region in a compute pass, or by writing
multiple times to a resource region. If your compute work depends on
reading the completed output from a previous dispatch, you MUST end the
current compute pass and begin a new one before you can safely access the
data. Otherwise you will receive unexpected results. Reading and writing a
texture in the same compute pass is only supported by specific texture
formats. Make sure you check the format support!

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_EndGPUComputePass](SDL_EndGPUComputePass)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

