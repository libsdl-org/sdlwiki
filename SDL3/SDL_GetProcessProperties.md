# SDL_GetProcessProperties

Get the properties associated with a process.

## Header File

Defined in [<SDL3/SDL_process.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_process.h)

## Syntax

```c
SDL_PropertiesID SDL_GetProcessProperties(SDL_Process *process);
```

## Function Parameters

|                              |             |                       |
| ---------------------------- | ----------- | --------------------- |
| [SDL_Process](SDL_Process) * | **process** | the process to query. |

## Return Value

([SDL_PropertiesID](SDL_PropertiesID)) Returns a valid property ID on
success or 0 on failure; call [SDL_GetError](SDL_GetError)() for more
information.

## Remarks

The following read-only properties are provided by SDL:

- [`SDL_PROP_PROCESS_PID_NUMBER`](SDL_PROP_PROCESS_PID_NUMBER): the process
  ID of the process.
- [`SDL_PROP_PROCESS_STDIN_POINTER`](SDL_PROP_PROCESS_STDIN_POINTER): an
  [SDL_IOStream](SDL_IOStream) that can be used to write input to the
  process, if it was created with
  [`SDL_PROP_PROCESS_CREATE_STDIN_NUMBER`](SDL_PROP_PROCESS_CREATE_STDIN_NUMBER)
  set to [`SDL_PROCESS_STDIO_APP`](SDL_PROCESS_STDIO_APP).
- [`SDL_PROP_PROCESS_STDOUT_POINTER`](SDL_PROP_PROCESS_STDOUT_POINTER): a
  non-blocking [SDL_IOStream](SDL_IOStream) that can be used to read output
  from the process, if it was created with
  [`SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER`](SDL_PROP_PROCESS_CREATE_STDOUT_NUMBER)
  set to [`SDL_PROCESS_STDIO_APP`](SDL_PROCESS_STDIO_APP).
- [`SDL_PROP_PROCESS_STDERR_POINTER`](SDL_PROP_PROCESS_STDERR_POINTER): a
  non-blocking [SDL_IOStream](SDL_IOStream) that can be used to read error
  output from the process, if it was created with
  [`SDL_PROP_PROCESS_CREATE_STDERR_NUMBER`](SDL_PROP_PROCESS_CREATE_STDERR_NUMBER)
  set to [`SDL_PROCESS_STDIO_APP`](SDL_PROCESS_STDIO_APP).
- [`SDL_PROP_PROCESS_BACKGROUND_BOOLEAN`](SDL_PROP_PROCESS_BACKGROUND_BOOLEAN):
  true if the process is running in the background.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CreateProcess](SDL_CreateProcess)
- [SDL_CreateProcessWithProperties](SDL_CreateProcessWithProperties)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryProcess](CategoryProcess)

