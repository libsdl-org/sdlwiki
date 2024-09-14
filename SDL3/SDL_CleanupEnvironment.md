###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CleanupEnvironment

Cleanup the process environment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void SDL_CleanupEnvironment(void);
```

## Remarks

This is called during [SDL_Quit](SDL_Quit)() to free the process
environment. If [SDL_GetEnvironment](SDL_GetEnvironment)() is called
afterwards, it will automatically create a new environment copied from the
C runtime environment.

## Thread Safety

This function is not thread-safe.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetEnvironment](SDL_GetEnvironment)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

