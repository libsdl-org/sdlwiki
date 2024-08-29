###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_BeginGpuCopyPass

Begins a copy pass on a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuCopyPass* SDL_BeginGpuCopyPass(
    SDL_GpuCommandBuffer *commandBuffer);
```

## Function Parameters

|                                                |                   |                   |
| ---------------------------------------------- | ----------------- | ----------------- |
| [SDL_GpuCommandBuffer](SDL_GpuCommandBuffer) * | **commandBuffer** | a command buffer. |

## Return Value

([SDL_GpuCopyPass](SDL_GpuCopyPass) *) Returns a copy pass handle.

## Remarks

All operations related to copying to or from buffers or textures take place
inside a copy pass. You must not begin another copy pass, or a render pass
or compute pass before ending the copy pass.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

