###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetEnvironment

Get the process environment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
SDL_Environment * SDL_GetEnvironment(void);
```

## Return Value

([SDL_Environment](SDL_Environment) *) Returns a pointer to the environment
for the process or NULL on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

This is initialized at application start and is not affected by setenv()
and unsetenv() calls after that point. Use
[SDL_SetEnvironmentVariable](SDL_SetEnvironmentVariable)() and
[SDL_UnsetEnvironmentVariable](SDL_UnsetEnvironmentVariable)() if you want
to modify this environment.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CleanupEnvironment](SDL_CleanupEnvironment)
- [SDL_GetEnvironmentVariable](SDL_GetEnvironmentVariable)
- [SDL_GetEnvironmentVariables](SDL_GetEnvironmentVariables)
- [SDL_SetEnvironmentVariable](SDL_SetEnvironmentVariable)
- [SDL_UnsetEnvironmentVariable](SDL_UnsetEnvironmentVariable)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

