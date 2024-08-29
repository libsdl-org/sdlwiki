###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGpuBuffer

Creates a buffer object to be used in graphics or compute workflows.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuBuffer* SDL_CreateGpuBuffer(
    SDL_GpuDevice *device,
    SDL_GpuBufferCreateInfo *bufferCreateInfo);
```

## Function Parameters

|                                                      |                      |                                                        |
| ---------------------------------------------------- | -------------------- | ------------------------------------------------------ |
| [SDL_GpuDevice](SDL_GpuDevice) *                     | **device**           | a GPU Context.                                         |
| [SDL_GpuBufferCreateInfo](SDL_GpuBufferCreateInfo) * | **bufferCreateInfo** | a struct describing the state of the buffer to create. |

## Return Value

([SDL_GpuBuffer](SDL_GpuBuffer) *) Returns a buffer object on success, or
NULL on failure.

## Remarks

The contents of this buffer are undefined until data is written to the
buffer.

Note that certain combinations of usage flags are invalid. For example, a
buffer cannot have both the VERTEX and INDEX flags.

## Version

This function is available since SDL 3.x.x

## See Also

- [SDL_UploadToGpuBuffer](SDL_UploadToGpuBuffer)
- [SDL_BindGpuVertexBuffers](SDL_BindGpuVertexBuffers)
- [SDL_BindGpuIndexBuffer](SDL_BindGpuIndexBuffer)
- [SDL_BindGpuVertexStorageBuffers](SDL_BindGpuVertexStorageBuffers)
- [SDL_BindGpuFragmentStorageBuffers](SDL_BindGpuFragmentStorageBuffers)
- [SDL_BindGpuComputeStorageBuffers](SDL_BindGpuComputeStorageBuffers)
- [SDL_ReleaseGpuBuffer](SDL_ReleaseGpuBuffer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

