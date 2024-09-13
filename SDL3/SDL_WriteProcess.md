###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_WriteProcess

Write to a process.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
SDL_bool SDL_WriteProcess(SDL_Process *process, const void *ptr, size_t size, SDL_bool closeio);
```

## Function Parameters

|                              |             |                                                                                                   |
| ---------------------------- | ----------- | ------------------------------------------------------------------------------------------------- |
| [SDL_Process](SDL_Process) * | **process** | The process to write.                                                                             |
| const void *                 | **ptr**     | a pointer to a buffer containing data to write.                                                   |
| size_t                       | **size**    | the number of bytes to write.                                                                     |
| [SDL_bool](SDL_bool)         | **closeio** | if [SDL_TRUE](SDL_TRUE), closes the process input before returning, even in the case of an error. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

If a process was created with I/O enabled, you can use this function to
send data as input to the process. This function blocks until the data is
written.

This is just a convenience function. If the process is structured so it
takes large amounts of input and generates lots of output, you should get
the input and output streams from the process properties and handle them
simultaneously to prevent the process from being blocked waiting for I/O.

## Thread Safety

This function is not thread safe.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CreateProcess](SDL_CreateProcess)
- [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)
- [SDL_GetProcessProperties](SDL_GetProcessProperties)
- [SDL_ReadProcess](SDL_ReadProcess)
- [SDL_DestroyProcess](SDL_DestroyProcess)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProcess](CategoryProcess)

