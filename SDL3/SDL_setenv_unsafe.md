# SDL_setenv_unsafe

Set the value of a variable in the environment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_setenv_unsafe(const char *name, const char *value, int overwrite);
```

## Function Parameters

|              |               |                                                                                                                  |
| ------------ | ------------- | ---------------------------------------------------------------------------------------------------------------- |
| const char * | **name**      | the name of the variable to set.                                                                                 |
| const char * | **value**     | the value of the variable to set.                                                                                |
| int          | **overwrite** | 1 to overwrite the variable if it exists, 0 to return success without setting the variable if it already exists. |

## Return Value

(int) Returns 0 on success, -1 on error.

## Thread Safety

This function is not thread safe, consider using
[SDL_SetEnvironmentVariable](SDL_SetEnvironmentVariable)() instead.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetEnvironmentVariable](SDL_SetEnvironmentVariable)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

