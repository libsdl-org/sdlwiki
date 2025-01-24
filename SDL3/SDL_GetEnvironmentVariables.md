# SDL_GetEnvironmentVariables

Get all variables in the environment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
char ** SDL_GetEnvironmentVariables(SDL_Environment *env);
```

## Function Parameters

|                                      |         |                           |
| ------------------------------------ | ------- | ------------------------- |
| [SDL_Environment](SDL_Environment) * | **env** | the environment to query. |

## Return Value

(char **) Returns a NULL terminated array of pointers to environment
variables in the form "variable=value" or NULL on failure; call
[SDL_GetError](SDL_GetError)() for more information. This is a single
allocation that should be freed with [SDL_free](SDL_free)() when it is no
longer needed.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetEnvironment](SDL_GetEnvironment)
- [SDL_CreateEnvironment](SDL_CreateEnvironment)
- [SDL_GetEnvironmentVariables](SDL_GetEnvironmentVariables)
- [SDL_SetEnvironmentVariable](SDL_SetEnvironmentVariable)
- [SDL_UnsetEnvironmentVariable](SDL_UnsetEnvironmentVariable)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

