###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ReadProcess

Read all the output from a process.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
void * SDL_ReadProcess(SDL_Process *process, size_t *datasize, int *exitcode);
```

## Function Parameters

|                              |              |                                                                                        |
| ---------------------------- | ------------ | -------------------------------------------------------------------------------------- |
| [SDL_Process](SDL_Process) * | **process**  | The process to read.                                                                   |
| size_t *                     | **datasize** | a pointer filled in with the number of bytes read, may be NULL.                        |
| int *                        | **exitcode** | a pointer filled in with the process exit code if the process has exited, may be NULL. |

## Return Value

(void *) Returns the data or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

If a process was created with I/O enabled, you can use this function to
read the output. This function blocks until the process is complete,
capturing all output, and providing the process exit code.

This is just a convenience function. If you need more control over the
process, you can get the output stream from the process properties and read
it directly.

The data is allocated with a zero byte at the end (null terminated) for
convenience. This extra byte is not included in the value reported via
`datasize`.

The data should be freed with [SDL_free](SDL_free)().

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateProcess](SDL_CreateProcess)
- [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)
- [SDL_GetProcessProperties](SDL_GetProcessProperties)
- [SDL_WriteProcess](SDL_WriteProcess)
- [SDL_DestroyProcess](SDL_DestroyProcess)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProcess](CategoryProcess)

