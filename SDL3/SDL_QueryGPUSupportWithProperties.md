###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_QueryGPUSupportWithProperties

Checks for GPU runtime support.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
SDL_bool SDL_QueryGPUSupportWithProperties(
    SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                        |
| ------------------------------------ | --------- | ---------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to use. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if supported,
[SDL_FALSE](SDL_FALSE) otherwise.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateGPUDeviceWithProperties](SDL_CreateGPUDeviceWithProperties)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

