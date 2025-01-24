# SDL_GetProcessOutput

Get the [SDL_IOStream](SDL_IOStream) associated with process standard output.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
SDL_IOStream* SDL_GetProcessOutput(SDL_Process *process);
```

## Function Parameters

|                              |             |                                           |
| ---------------------------- | ----------- | ----------------------------------------- |
| [SDL_Process](SDL_Process) * | **process** | The process to get the output stream for. |

## Return Value

([SDL_IOStream](SDL_IOStream) *) Returns the output stream or NULL on
failure; call [SDL_GetError](SDL_GetError)() for more information.

## Remarks

The process must have been created with
[SDL_CreateProcess](SDL_CreateProcess)() and pipe_stdio set to true, or
with [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)()
and
[`SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER`](SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER)
set to [`SDL_PROCESS_STDIO_APP`](SDL_PROCESS_STDIO_APP).

Reading from this stream can return 0 with
[SDL_GetIOStatus](SDL_GetIOStatus)() returning
[SDL_IO_STATUS_NOT_READY](SDL_IO_STATUS_NOT_READY) if no output is
available yet.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateProcess](SDL_CreateProcess)
- [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)
- [SDL_GetProcessInput](SDL_GetProcessInput)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProcess](CategoryProcess)

