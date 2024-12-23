###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CreateGPUBuffer

Creates a buffer object to be used in graphics or compute workflows.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUBuffer* SDL_CreateGPUBuffer(
    SDL_GPUDevice *device,
    const SDL_GPUBufferCreateInfo *createinfo);
```

## Function Parameters

|                                                            |                |                                                        |
| ---------------------------------------------------------- | -------------- | ------------------------------------------------------ |
| [SDL_GPUDevice](SDL_GPUDevice) *                           | **device**     | a GPU Context.                                         |
| const [SDL_GPUBufferCreateInfo](SDL_GPUBufferCreateInfo) * | **createinfo** | a struct describing the state of the buffer to create. |

## Return Value

([SDL_GPUBuffer](SDL_GPUBuffer) *) Returns a buffer object on success, or
NULL on failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The contents of this buffer are undefined until data is written to the
buffer.

Note that certain combinations of usage flags are invalid. For example, a
buffer cannot have both the VERTEX and INDEX flags.

For better understanding of underlying concepts and memory management with
SDL GPU API, you may refer
[this blog post](https://moonside.games/posts/sdl-gpu-concepts-cycling/)
.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SetGPUBufferName](SDL_SetGPUBufferName)
- [SDL_UploadToGPUBuffer](SDL_UploadToGPUBuffer)
- [SDL_DownloadFromGPUBuffer](SDL_DownloadFromGPUBuffer)
- [SDL_CopyGPUBufferToBuffer](SDL_CopyGPUBufferToBuffer)
- [SDL_BindGPUVertexBuffers](SDL_BindGPUVertexBuffers)
- [SDL_BindGPUIndexBuffer](SDL_BindGPUIndexBuffer)
- [SDL_BindGPUVertexStorageBuffers](SDL_BindGPUVertexStorageBuffers)
- [SDL_BindGPUFragmentStorageBuffers](SDL_BindGPUFragmentStorageBuffers)
- [SDL_DrawGPUPrimitivesIndirect](SDL_DrawGPUPrimitivesIndirect)
- [SDL_DrawGPUIndexedPrimitivesIndirect](SDL_DrawGPUIndexedPrimitivesIndirect)
- [SDL_BindGPUComputeStorageBuffers](SDL_BindGPUComputeStorageBuffers)
- [SDL_DispatchGPUComputeIndirect](SDL_DispatchGPUComputeIndirect)
- [SDL_ReleaseGPUBuffer](SDL_ReleaseGPUBuffer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

