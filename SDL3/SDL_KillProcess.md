###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_KillProcess

Stop a process.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
bool SDL_KillProcess(SDL_Process *process, bool force);
```

## Function Parameters

|                              |             |                                                                                                                                                                                                                                                      |
| ---------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [SDL_Process](SDL_Process) * | **process** | The process to stop.                                                                                                                                                                                                                                 |
| bool                         | **force**   | true to terminate the process immediately, false to try to stop the process gracefully. In general you should try to stop the process gracefully first as terminating a process may leave it with half-written data or in some other unstable state. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateProcess](SDL_CreateProcess)
- [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)
- [SDL_WaitProcess](SDL_WaitProcess)
- [SDL_DestroyProcess](SDL_DestroyProcess)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProcess](CategoryProcess)

