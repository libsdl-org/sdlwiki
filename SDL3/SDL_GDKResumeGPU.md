# SDL_GDKResumeGPU

Call this to resume GPU operation on Xbox when you receive the [SDL_EVENT_WILL_ENTER_FOREGROUND](SDL_EVENT_WILL_ENTER_FOREGROUND) event.

## Header File

Defined in [<SDL3/SDL_gpu.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_gpu.h)

## Syntax

```c
void SDL_GDKResumeGPU(SDL_GPUDevice *device);
```

## Function Parameters

|                                  |            |                |
| -------------------------------- | ---------- | -------------- |
| [SDL_GPUDevice](SDL_GPUDevice) * | **device** | a GPU context. |

## Remarks

When resuming, this function MUST be called before calling any other
[SDL_GPU](SDL_GPU) functions.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_AddEventWatch](SDL_AddEventWatch)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryGPU](CategoryGPU)

