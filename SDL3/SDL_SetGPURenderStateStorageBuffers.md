# SDL_SetGPURenderStateStorageBuffers

Set storage buffers variables in a custom GPU render state.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetGPURenderStateStorageBuffers(SDL_GPURenderState *state, int num_storage_buffers, SDL_GPUBuffer *const *storage_buffers);
```

## Function Parameters

|                                            |                         |                                        |
| ------------------------------------------ | ----------------------- | -------------------------------------- |
| [SDL_GPURenderState](SDL_GPURenderState) * | **state**               | the state to modify.                   |
| int                                        | **num_storage_buffers** | The number of storage buffers to bind. |
| [SDL_GPUBuffer](SDL_GPUBuffer) *const *    | **storage_buffers**     | Storage buffers to bind.               |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The data is copied and will be binded using
[SDL_BindGPUFragmentStorageBuffers](SDL_BindGPUFragmentStorageBuffers)()
during draw call execution.

## Thread Safety

This function should be called on the thread that created the renderer.

## Version

This function is available since SDL 3.4.x.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

