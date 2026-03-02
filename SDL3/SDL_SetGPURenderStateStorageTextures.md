# SDL_SetGPURenderStateStorageTextures

Set storage textures variables in a custom GPU render state.

## Header File

Defined in [<SDL3/SDL_render.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_render.h)

## Syntax

```c
bool SDL_SetGPURenderStateStorageTextures(SDL_GPURenderState *state, int num_storage_textures, SDL_GPUTexture *const *storage_textures);
```

## Function Parameters

|                                            |                          |                                         |
| ------------------------------------------ | ------------------------ | --------------------------------------- |
| [SDL_GPURenderState](SDL_GPURenderState) * | **state**                | the state to modify.                    |
| int                                        | **num_storage_textures** | The number of storage textures to bind. |
| [SDL_GPUTexture](SDL_GPUTexture) *const *  | **storage_textures**     | Storage textures to bind.               |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

The data is copied and will be binded using
[SDL_BindGPUFragmentStorageTextures](SDL_BindGPUFragmentStorageTextures)()
during draw call execution.

## Thread Safety

This function should be called on the thread that created the renderer.

## Version

This function is available since SDL 3.4.x.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryRender](CategoryRender)

