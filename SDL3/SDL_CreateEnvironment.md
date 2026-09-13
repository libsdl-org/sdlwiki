# SDL_CreateEnvironment

Create a set of environment variables.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
SDL_Environment * SDL_CreateEnvironment(bool populated);
```

## Function Parameters

|      |               |                                                                                             |
| ---- | ------------- | ------------------------------------------------------------------------------------------- |
| bool | **populated** | true to initialize it from the C runtime environment, false to create an empty environment. |

## Return Value

([SDL_Environment](SDL_Environment) *) Returns a pointer to the new
environment or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

Note that on Windows, the variable names pulled in from the system, if
`populated` is true, have their ASCII values uppercased, to match what most
platforms expect even though the Windows system environment table is
case-insensitive. Once those uppercased variable names are in an
[SDL_Environment](SDL_Environment), SDL treats them as case-sensitive.

## Thread Safety

If `populated` is false, it is safe to call this function from any thread,
otherwise it is safe if no other threads are calling setenv() or unsetenv()

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetEnvironmentVariable](SDL_GetEnvironmentVariable)
- [SDL_GetEnvironmentVariables](SDL_GetEnvironmentVariables)
- [SDL_SetEnvironmentVariable](SDL_SetEnvironmentVariable)
- [SDL_UnsetEnvironmentVariable](SDL_UnsetEnvironmentVariable)
- [SDL_DestroyEnvironment](SDL_DestroyEnvironment)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

