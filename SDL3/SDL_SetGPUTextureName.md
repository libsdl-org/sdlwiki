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

Useful for debugging.

## Thread Safety

This function is not thread safe, you must synchronize calls to this
function.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

