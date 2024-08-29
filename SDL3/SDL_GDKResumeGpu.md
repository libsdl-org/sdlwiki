###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GDKResumeGpu

Call this to resume GPU operation on Xbox when you receive the [SDL_EVENT_WILL_ENTER_FOREGROUND](SDL_EVENT_WILL_ENTER_FOREGROUND) event.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_GDKResumeGpu(SDL_GpuDevice *device);
```

## Function Parameters

|                                  |            |                |
| -------------------------------- | ---------- | -------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU context. |

## Remarks

When resuming, this function MUST be called before calling any other
[SDL_Gpu](SDL_Gpu) functions.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AddEventWatch](SDL_AddEventWatch)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU), [CategoryGpu](CategoryGpu)


