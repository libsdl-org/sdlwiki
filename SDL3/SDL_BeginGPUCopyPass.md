###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BeginGPUCopyPass

Begins a copy pass on a command buffer.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GPUCopyPass* SDL_BeginGPUCopyPass(
    SDL_GPUCommandBuffer *command_buffer);
```

## Function Parameters

|                                                |                    |                   |
| ---------------------------------------------- | ------------------ | ----------------- |
| [SDL_GPUCommandBuffer](SDL_GPUCommandBuffer) * | **command_buffer** | a command buffer. |

## Return Value

([SDL_GPUCopyPass](SDL_GPUCopyPass) *) Returns a copy pass handle.

## Remarks

All operations related to copying to or from buffers or textures take place
inside a copy pass. You must not begin another copy pass, or a render pass
or compute pass before ending the copy pass.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

