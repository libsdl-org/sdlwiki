# SDL_BindGPUFragmentStorageBuffers

Binds storage buffers for use on the fragment shader.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_BindGPUFragmentStorageBuffers(
    SDL_GPURenderPass *render_pass,
    Uint32 first_slot,
    SDL_GPUBuffer *const *storage_buffers,
    Uint32 num_bindings);
```

## Function Parameters

|                                          |                     |                                                         |
| ---------------------------------------- | ------------------- | ------------------------------------------------------- |
| [SDL_GPURenderPass](SDL_GPURenderPass) * | **render_pass**     | a render pass handle.                                   |
| [Uint32](Uint32)                         | **first_slot**      | the fragment storage buffer slot to begin binding from. |
| [SDL_GPUBuffer](SDL_GPUBuffer) *const *  | **storage_buffers** | an array of storage buffers.                            |
| [Uint32](Uint32)                         | **num_bindings**    | the number of storage buffers to bind from the array.   |

## Remarks

These buffers must have been created with
[SDL_GPU_BUFFERUSAGE_GRAPHICS_STORAGE_READ](SDL_GPU_BUFFERUSAGE_GRAPHICS_STORAGE_READ).

Be sure your shader is set up according to the requirements documented in
[SDL_CreateGPUShader](SDL_CreateGPUShader)().

first_slot != binding number. 
Even if binding=2 for your first frag storage buffer, you should still use first_slot=0.
Use first_slot as a way to skip binding the first X frag storage buffers, then in that case, set first_slot=X.
If you instead use the binding number, and go out of bounds due to this, 
you will incur a seg fault in any subsequent draw calls, at least in Vulkan.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUShader](SDL_CreateGPUShader)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

