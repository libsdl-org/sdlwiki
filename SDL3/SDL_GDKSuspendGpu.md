###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GDKSuspendGpu

Call this to suspend GPU operation on Xbox when you receive the [SDL_EVENT_DID_ENTER_BACKGROUND](SDL_EVENT_DID_ENTER_BACKGROUND) event.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_GDKSuspendGpu(SDL_GpuDevice *device);
```

## Function Parameters

|                                  |            |                |
| -------------------------------- | ---------- | -------------- |
| [SDL_GpuDevice](SDL_GpuDevice) * | **device** | a GPU context. |

## Remarks

Do NOT call any [SDL_Gpu](SDL_Gpu) functions after calling this function!
This must also be called before calling
[SDL_GDKSuspendComplete](SDL_GDKSuspendComplete).

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AddEventWatch](SDL_AddEventWatch)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGpu](CategoryGpu)

