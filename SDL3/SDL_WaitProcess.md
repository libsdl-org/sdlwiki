###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WaitProcess

Wait for a process to finish.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
SDL_bool SDL_WaitProcess(SDL_Process *process, SDL_bool block, int *exitcode);
```

## Function Parameters

|                              |              |                                                                                        |
| ---------------------------- | ------------ | -------------------------------------------------------------------------------------- |
| [SDL_Process](SDL_Process) * | **process**  | The process to wait for.                                                               |
| [SDL_bool](SDL_bool)         | **block**    | If true, block until the process finishes; otherwise, report on the process' status.   |
| int *                        | **exitcode** | a pointer filled in with the process exit code if the process has exited, may be NULL. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the process exited,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

This can be called multiple times to get the status of a process.

The exit code will be the exit code of the process if it terminates
normally, a negative signal if it terminated due to a signal, or -255
otherwise. It will not be changed if the process is still running.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateProcess](SDL_CreateProcess)
- [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)
- [SDL_KillProcess](SDL_KillProcess)
- [SDL_DestroyProcess](SDL_DestroyProcess)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProcess](CategoryProcess)

