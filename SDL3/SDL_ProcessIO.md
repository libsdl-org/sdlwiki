###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ProcessIO

Description of where standard I/O should be directed when creating a process.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
typedef enum SDL_ProcessIO
{
    SDL_PROCESS_STDIO_INHERITED,    /**< The I/O stream is inherited from the application. */
    SDL_PROCESS_STDIO_NULL,         /**< The I/O stream is ignored. */
    SDL_PROCESS_STDIO_APP,          /**< The I/O stream is connected to a new SDL_IOStream that the application can read or write */
    SDL_PROCESS_STDIO_REDIRECT,     /**< The I/O stream is redirected to an existing SDL_IOStream. */
} SDL_ProcessIO;
```

## Remarks

If a standard I/O stream is set to
[SDL_PROCESS_STDIO_INHERIT](SDL_PROCESS_STDIO_INHERIT), it will go to the
same place as the application's I/O stream. This is the default for
standard output and standard error.

If a standard I/O stream is set to
[SDL_PROCESS_STDIO_NULL](SDL_PROCESS_STDIO_NULL), it is connected to `NUL:`
on Windows and `/dev/null` on POSIX systems. This is the default for
standard input.

If a standard I/O stream is set to
[SDL_PROCESS_STDIO_APP](SDL_PROCESS_STDIO_APP), it is connected to a new
[SDL_IOStream](SDL_IOStream) that is available to the application. Standard
input will be available as
[`SDL_PROP_PROCESS_STDIN_POINTER`](SDL_PROP_PROCESS_STDIN_POINTER) and
allows [SDL_WriteProcess](SDL_WriteProcess)(), standard output will be
available as
[`SDL_PROP_PROCESS_STDOUT_POINTER`](SDL_PROP_PROCESS_STDOUT_POINTER) and
allows [SDL_ReadProcess](SDL_ReadProcess)(), and standard error will be
available as
[`SDL_PROP_PROCESS_STDERR_POINTER`](SDL_PROP_PROCESS_STDERR_POINTER) in the
properties for the created process.

If a standard I/O stream is set to
[SDL_PROCESS_STDIO_REDIRECT](SDL_PROCESS_STDIO_REDIRECT), it is connected
to an existing [SDL_IOStream](SDL_IOStream) provided by the application.
Standard input is provided using
[`SDL_PROP_PROCESS_CREATE_STDIN_POINTER`](SDL_PROP_PROCESS_CREATE_STDIN_POINTER),
standard output is provided using
[`SDL_PROP_PROCESS_CREATE_STDOUT_POINTER`](SDL_PROP_PROCESS_CREATE_STDOUT_POINTER),
and standard error is provided using
[`SDL_PROP_PROCESS_CREATE_STDERR_POINTER`](SDL_PROP_PROCESS_CREATE_STDERR_POINTER)
in the creation properties. These existing streams should be closed by the
application once the new process is created.

In order to use an [SDL_IOStream](SDL_IOStream) with
[SDL_PROCESS_STDIO_REDIRECT](SDL_PROCESS_STDIO_REDIRECT), it must have
[`SDL_PROP_IOSTREAM_WINDOWS_HANDLE_POINTER`](SDL_PROP_IOSTREAM_WINDOWS_HANDLE_POINTER)
or
[`SDL_PROP_IOSTREAM_FILE_DESCRIPTOR_NUMBER`](SDL_PROP_IOSTREAM_FILE_DESCRIPTOR_NUMBER)
set. This is true for streams representing files and process I/O.

## Version

This enum is available since SDL 3.0.0.

## See Also

- [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)
- [SDL_GetProcessProperties](SDL_GetProcessProperties)
- [SDL_ReadProcess](SDL_ReadProcess)
- [SDL_WriteProcess](SDL_WriteProcess)

----
[CategoryAPI](CategoryAPI), [CategoryAPIEnum](CategoryAPIEnum), [CategoryProcess](CategoryProcess)

