# SDL_GetGPUDriver

Get the name of a built in GPU driver.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
const char * SDL_GetGPUDriver(int index);
```

## Function Parameters

|     |           |                            |
| --- | --------- | -------------------------- |
| int | **index** | the index of a GPU driver. |

## Return Value

(const char *) Returns the name of the GPU driver with the given **index**.

## Remarks

The GPU drivers are presented in the order in which they are normally
checked during initialization.

The names of drivers are all simple, low-ASCII identifiers, like "vulkan",
"metal" or "direct3d12". These never have Unicode characters, and are not
meant to be proper names.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetNumGPUDrivers](SDL_GetNumGPUDrivers)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

