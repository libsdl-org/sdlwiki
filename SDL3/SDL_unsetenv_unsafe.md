###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_unsetenv_unsafe

Clear a variable from the environment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
int SDL_unsetenv_unsafe(const char *name);
```

## Function Parameters

|              |          |                                    |
| ------------ | -------- | ---------------------------------- |
| const char * | **name** | the name of the variable to unset. |

## Return Value

(int) Returns 0 on success, -1 on error.

## Thread Safety

This function is not thread safe, consider using
[SDL_UnsetEnvironmentVariable](SDL_UnsetEnvironmentVariable)() instead..

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_UnsetEnvironmentVariable](SDL_UnsetEnvironmentVariable)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

