###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetGPUTextureName

Sets an arbitrary string constant to label a texture.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_SetGPUTextureName(
    SDL_GPUDevice *device,
    SDL_GPUTexture *texture,
    const char *text);
```

## Function Parameters

|                                    |             |                                                             |
| ---------------------------------- | ----------- | ----------------------------------------------------------- |
| [SDL_GPUDevice](SDL_GPUDevice) *   | **device**  | a GPU Context.                                              |
| [SDL_GPUTexture](SDL_GPUTexture) * | **texture** | a texture to attach the name to.                            |
| const char *                       | **text**    | a UTF-8 string constant to mark as the name of the texture. |

## Remarks

You should use
[SDL_PROP_GPU_TEXTURE_CREATE_NAME_STRING](SDL_PROP_GPU_TEXTURE_CREATE_NAME_STRING)
with [SDL_CreateGPUTexture](SDL_CreateGPUTexture) instead of this function
to avoid thread safety issues.

## Thread Safety

This function is not thread safe, you must make sure the texture is not
simultaneously used by any other thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateGPUTexture](SDL_CreateGPUTexture)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

