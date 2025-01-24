# SDL_GetEnvironmentVariable

Get the value of a variable in the environment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
const char * SDL_GetEnvironmentVariable(SDL_Environment *env, const char *name);
```

## Function Parameters

|                                      |          |                                  |
| ------------------------------------ | -------- | -------------------------------- |
| [SDL_Environment](SDL_Environment) * | **env**  | the environment to query.        |
| const char *                         | **name** | the name of the variable to get. |

## Return Value

(const char *) Returns a pointer to the value of the variable or NULL if it
can't be found.

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

