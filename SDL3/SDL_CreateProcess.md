###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateProcess

Create a new process.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
SDL_Process* SDL_CreateProcess(const char * const *args, SDL_bool pipe_stdio);
```

## Function Parameters

|                      |                |                                                                                                                                                                                                                     |
| -------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| const char * const * | **args**       | the path and arguments for the new process.                                                                                                                                                                         |
| [SDL_bool](SDL_bool) | **pipe_stdio** | [SDL_TRUE](SDL_TRUE) to create pipes to the process's standard input and from the process's standard output, [SDL_FALSE](SDL_FALSE) for the process to have no input and inherit the application's standard output. |

## Return Value

([SDL_Process](SDL_Process) *) Returns the newly created and running
process, or NULL if the process couldn't be created.

## Remarks

The path to the executable is supplied in args[0]. args[1..N] are
additional arguments passed on the command line of the new process, and the
argument list should be terminated with a NULL, e.g.:

```c
const char *args[] = { "myprogram", "argument", NULL };
```

Setting pipe_stdio to [SDL_TRUE](SDL_TRUE) is equivalent to setting
[`SDL_PROP_PROCESS_CREATE_STDIN_NUMBER`](SDL_PROP_PROCESS_CREATE_STDIN_NUMBER)
and
[`SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER`](SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER)
to [`SDL_PROCESS_STDIO_APP`](SDL_PROCESS_STDIO_APP), and will allow the use
of [SDL_ReadProcess](SDL_ReadProcess)() or
[SDL_GetProcessInput](SDL_GetProcessInput)() and
[SDL_GetProcessOutput](SDL_GetProcessOutput)().

See [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)()
for more details.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)
- [SDL_GetProcessProperties](SDL_GetProcessProperties)
- [SDL_ReadProcess](SDL_ReadProcess)
- [SDL_GetProcessInput](SDL_GetProcessInput)
- [SDL_GetProcessOutput](SDL_GetProcessOutput)
- [SDL_KillProcess](SDL_KillProcess)
- [SDL_WaitProcess](SDL_WaitProcess)
- [SDL_DestroyProcess](SDL_DestroyProcess)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProcess](CategoryProcess)

