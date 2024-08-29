###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateGpuDevice

Creates a GPU context.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_GpuDevice* SDL_CreateGpuDevice(
    SDL_GpuShaderFormat formatFlags,
    SDL_bool debugMode,
    SDL_bool preferLowPower,
    const char *name);
```

## Function Parameters

|                                            |                    |                                                                                                      |
| ------------------------------------------ | ------------------ | ---------------------------------------------------------------------------------------------------- |
| [SDL_GpuShaderFormat](SDL_GpuShaderFormat) | **formatFlags**    | a bitflag indicating which shader formats the app is able to provide.                                |
| [SDL_bool](SDL_bool)                       | **debugMode**      | enable debug mode properties and validations.                                                        |
| [SDL_bool](SDL_bool)                       | **preferLowPower** | set this to [SDL_TRUE](SDL_TRUE) if your app prefers energy efficiency over maximum GPU performance. |
| const char *                               | **name**           | the preferred GPU driver, or NULL to let SDL pick the optimal driver.                                |

## Return Value

([SDL_GpuDevice](SDL_GpuDevice) *) Returns a GPU context on success or NULL
on failure.

## Version

This function is available since SDL 3.x.x

## See Also

- [SDL_GetGpuDriver](SDL_GetGpuDriver)
- [SDL_DestroyGpuDevice](SDL_DestroyGpuDevice)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

