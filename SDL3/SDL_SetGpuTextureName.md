###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetGpuTextureName

Sets an arbitrary string constant to label a texture.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_SetGpuTextureName(
    SDL_GpuDevice *device,
    SDL_GpuTexture *texture,
    const char *text);
```

## Function Parameters

|                                    |             |                                                             |
| ---------------------------------- | ----------- | ----------------------------------------------------------- |
| [SDL_GpuDevice](SDL_GpuDevice) *   | **device**  | a GPU Context.                                              |
| [SDL_GpuTexture](SDL_GpuTexture) * | **texture** | a texture to attach the name to.                            |
| const char *                       | **text**    | a UTF-8 string constant to mark as the name of the texture. |

## Remarks

Useful for debugging.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

