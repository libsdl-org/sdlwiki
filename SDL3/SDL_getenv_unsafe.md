###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_getenv_unsafe

Get the value of a variable in the environment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
const char * SDL_getenv_unsafe(const char *name);
```

## Function Parameters

|              |          |                                  |
| ------------ | -------- | -------------------------------- |
| const char * | **name** | the name of the variable to get. |

## Return Value

(const char *) Returns a pointer to the value of the variable or NULL if it
can't be found.

## Thread Safety

This function is not thread safe, consider using
[SDL_GetEnvironmentVariable](SDL_GetEnvironmentVariable)() instead.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetEnvironmentVariable](SDL_GetEnvironmentVariable)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

