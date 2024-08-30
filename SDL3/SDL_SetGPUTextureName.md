###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

