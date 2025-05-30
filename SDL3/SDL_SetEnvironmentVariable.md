# SDL_SetEnvironmentVariable

Set the value of a variable in the environment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
bool SDL_SetEnvironmentVariable(SDL_Environment *env, const char *name, const char *value, bool overwrite);
```

## Function Parameters

|                                      |               |                                                                                                                         |
| ------------------------------------ | ------------- | ----------------------------------------------------------------------------------------------------------------------- |
| [SDL_Environment](SDL_Environment) * | **env**       | the environment to modify.                                                                                              |
| const char *                         | **name**      | the name of the variable to set.                                                                                        |
| const char *                         | **value**     | the value of the variable to set.                                                                                       |
| bool                                 | **overwrite** | true to overwrite the variable if it exists, false to return success without setting the variable if it already exists. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetEnvironment](SDL_GetEnvironment)
- [SDL_CreateEnvironment](SDL_CreateEnvironment)
- [SDL_GetEnvironmentVariable](SDL_GetEnvironmentVariable)
- [SDL_GetEnvironmentVariables](SDL_GetEnvironmentVariables)
- [SDL_UnsetEnvironmentVariable](SDL_UnsetEnvironmentVariable)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

