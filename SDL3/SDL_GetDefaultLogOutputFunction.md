###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_GetDefaultLogOutputFunction

Get the default log output function.

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
SDL_LogOutputFunction SDL_GetDefaultLogOutputFunction(void);
```

## Return Value

([SDL_LogOutputFunction](SDL_LogOutputFunction)) Returns the default log
output callback.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetLogOutputFunction](SDL_SetLogOutputFunction)
- [SDL_GetLogOutputFunction](SDL_GetLogOutputFunction)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

