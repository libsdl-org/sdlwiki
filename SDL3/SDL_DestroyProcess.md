# SDL_DestroyProcess

Destroy a previously created process object.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
void SDL_DestroyProcess(SDL_Process *process);
```

## Function Parameters

|                              |             |                                |
| ---------------------------- | ----------- | ------------------------------ |
| [SDL_Process](SDL_Process) * | **process** | The process object to destroy. |

## Remarks

Note that this does not stop the process, just destroys the SDL object used
to track it. If you want to stop the process you should use
[SDL_KillProcess](SDL_KillProcess)().

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateProcess](SDL_CreateProcess)
- [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)
- [SDL_KillProcess](SDL_KillProcess)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProcess](CategoryProcess)

