###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CreateEnvironment

Create a set of environment variables.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
SDL_Environment * SDL_CreateEnvironment(SDL_bool populated);
```

## Function Parameters

|                      |               |                                                                                                                              |
| -------------------- | ------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| [SDL_bool](SDL_bool) | **populated** | [SDL_TRUE](SDL_TRUE) to initialize it from the C runtime environment, [SDL_FALSE](SDL_FALSE) to create an empty environment. |

## Return Value

([SDL_Environment](SDL_Environment) *) Returns a pointer to the new
environment or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Thread Safety

If `empty` is [SDL_TRUE](SDL_TRUE), it is safe to call this function from
any thread, otherwise it is safe if no other threads are calling setenv()
or unsetenv()

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetEnvironmentVariable](SDL_GetEnvironmentVariable)
- [SDL_GetEnvironmentVariables](SDL_GetEnvironmentVariables)
- [SDL_SetEnvironmentVariable](SDL_SetEnvironmentVariable)
- [SDL_UnsetEnvironmentVariable](SDL_UnsetEnvironmentVariable)
- [SDL_DestroyEnvironment](SDL_DestroyEnvironment)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

