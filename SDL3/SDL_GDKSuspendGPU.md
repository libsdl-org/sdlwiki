###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GDKSuspendGPU

Call this to suspend GPU operation on Xbox when you receive the [SDL_EVENT_DID_ENTER_BACKGROUND](SDL_EVENT_DID_ENTER_BACKGROUND) event.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_GDKSuspendGPU(SDL_GPUDevice *device);
```

## Function Parameters

|                                  |            |                |
| -------------------------------- | ---------- | -------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context. |

## Remarks

Do NOT call any [SDL_GPU](SDL_GPU) functions after calling this function!
This must also be called before calling
[SDL_GDKSuspendComplete](SDL_GDKSuspendComplete).

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AddEventWatch](SDL_AddEventWatch)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

