# SDL_CreateProcessWithProperties

Create a new process with the specified properties.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
SDL_Process * SDL_CreateProcessWithProperties(SDL_PropertiesID props);
```

## Function Parameters

|                                      |           |                        |
| ------------------------------------ | --------- | ---------------------- |
| [SDL_PropertiesID](SDL_PropertiesID) | **props** | the properties to use. |

## Return Value

([SDL_Process](SDL_Process) *) Returns the newly created and running
process, or NULL if the process couldn't be created.

## Remarks

These are the supported properties:

- [`SDL_PROP_PROCESS_CREATE_ARGS_POINTER`](SDL_PROP_PROCESS_CREATE_ARGS_POINTER):
  an array of strings containing the program to run, any arguments, and a
  NULL pointer, e.g. const char *args[] = { "myprogram", "argument", NULL
  }. This is a required property.
- [`SDL_PROP_PROCESS_CREATE_ENVIRONMENT_POINTER`](SDL_PROP_PROCESS_CREATE_ENVIRONMENT_POINTER):
  an [SDL_Environment](SDL_Environment) pointer. If this property is set,
  it will be the entire environment for the process, otherwise the current
  environment is used.
- [`SDL_PROP_PROCESS_CREATE_WORKING_DIRECTORY_STRING`](SDL_PROP_PROCESS_CREATE_WORKING_DIRECTORY_STRING):
  a UTF-8 encoded string representing the working directory for the
  process, defaults to the current working directory.
- [`SDL_PROP_PROCESS_CREATE_STDIN_NUMBER`](SDL_PROP_PROCESS_CREATE_STDIN_NUMBER):
  an [SDL_ProcessIO](SDL_ProcessIO) value describing where standard input
  for the process comes from, defaults to
  [`SDL_PROCESS_STDIO_NULL`](SDL_PROCESS_STDIO_NULL).
- [`SDL_PROP_PROCESS_CREATE_STDIN_POINTER`](SDL_PROP_PROCESS_CREATE_STDIN_POINTER):
  an [SDL_IOStream](SDL_IOStream) pointer used for standard input when
  [`SDL_PROP_PROCESS_CREATE_STDIN_NUMBER`](SDL_PROP_PROCESS_CREATE_STDIN_NUMBER)
  is set to [`SDL_PROCESS_STDIO_REDIRECT`](SDL_PROCESS_STDIO_REDIRECT).
- [`SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER`](SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER):
  an [SDL_ProcessIO](SDL_ProcessIO) value describing where standard output
  for the process goes to, defaults to
  [`SDL_PROCESS_STDIO_INHERITED`](SDL_PROCESS_STDIO_INHERITED).
- [`SDL_PROP_PROCESS_CREATE_STDOUT_POINTER`](SDL_PROP_PROCESS_CREATE_STDOUT_POINTER):
  an [SDL_IOStream](SDL_IOStream) pointer used for standard output when
  [`SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER`](SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER)
  is set to [`SDL_PROCESS_STDIO_REDIRECT`](SDL_PROCESS_STDIO_REDIRECT).
- [`SDL_PROP_PROCESS_CREATE_STDERR_NUMBER`](SDL_PROP_PROCESS_CREATE_STDERR_NUMBER):
  an [SDL_ProcessIO](SDL_ProcessIO) value describing where standard error
  for the process goes to, defaults to
  [`SDL_PROCESS_STDIO_INHERITED`](SDL_PROCESS_STDIO_INHERITED).
- [`SDL_PROP_PROCESS_CREATE_STDERR_POINTER`](SDL_PROP_PROCESS_CREATE_STDERR_POINTER):
  an [SDL_IOStream](SDL_IOStream) pointer used for standard error when
  [`SDL_PROP_PROCESS_CREATE_STDERR_NUMBER`](SDL_PROP_PROCESS_CREATE_STDERR_NUMBER)
  is set to [`SDL_PROCESS_STDIO_REDIRECT`](SDL_PROCESS_STDIO_REDIRECT).
- [`SDL_PROP_PROCESS_CREATE_STDERR_TO_STDOUT_BOOLEAN`](SDL_PROP_PROCESS_CREATE_STDERR_TO_STDOUT_BOOLEAN):
  true if the error output of the process should be redirected into the
  standard output of the process. This property has no effect if
  [`SDL_PROP_PROCESS_CREATE_STDERR_NUMBER`](SDL_PROP_PROCESS_CREATE_STDERR_NUMBER)
  is set.
- [`SDL_PROP_PROCESS_CREATE_BACKGROUND_BOOLEAN`](SDL_PROP_PROCESS_CREATE_BACKGROUND_BOOLEAN):
  true if the process should run in the background. In this case the
  default input and output is
  [`SDL_PROCESS_STDIO_NULL`](SDL_PROCESS_STDIO_NULL) and the exitcode of
  the process is not available, and will always be 0.

On POSIX platforms, wait() and waitpid(-1, ...) should not be called, and
SIGCHLD should not be ignored or handled because those would prevent SDL
from properly tracking the lifetime of the underlying process. You should
use [SDL_WaitProcess](SDL_WaitProcess)() instead.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateProcess](SDL_CreateProcess)
- [SDL_GetProcessProperties](SDL_GetProcessProperties)
- [SDL_ReadProcess](SDL_ReadProcess)
- [SDL_GetProcessInput](SDL_GetProcessInput)
- [SDL_GetProcessOutput](SDL_GetProcessOutput)
- [SDL_KillProcess](SDL_KillProcess)
- [SDL_WaitProcess](SDL_WaitProcess)
- [SDL_DestroyProcess](SDL_DestroyProcess)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProcess](CategoryProcess)

