# SDL_WaitProcess

Wait for a process to finish.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
bool SDL_WaitProcess(SDL_Process *process, bool block, int *exitcode);
```

## Function Parameters

|                              |              |                                                                                        |
| ---------------------------- | ------------ | -------------------------------------------------------------------------------------- |
| [SDL_Process](SDL_Process) * | **process**  | The process to wait for.                                                               |
| bool                         | **block**    | If true, block until the process finishes; otherwise, report on the process' status.   |
| int *                        | **exitcode** | a pointer filled in with the process exit code if the process has exited, may be NULL. |

## Return Value

(bool) Returns true if the process exited, false otherwise.

## Remarks

This can be called multiple times to get the status of a process.

The exit code will be the exit code of the process if it terminates
normally, a negative signal if it terminated due to a signal, or -255
otherwise. It will not be changed if the process is still running.

If you create a process with standard output piped to the application
(`pipe_stdio` being true) then you should read all of the process output
before calling [SDL_WaitProcess](SDL_WaitProcess)(). If you don't do this
the process might be blocked indefinitely waiting for output to be read and
[SDL_WaitProcess](SDL_WaitProcess)() will never return true;

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateProcess](SDL_CreateProcess)
- [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)
- [SDL_KillProcess](SDL_KillProcess)
- [SDL_DestroyProcess](SDL_DestroyProcess)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProcess](CategoryProcess)

