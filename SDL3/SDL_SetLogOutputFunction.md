###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetLogOutputFunction

Replace the default log output function with one of your own.

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
void SDL_SetLogOutputFunction(SDL_LogOutputFunction callback, void *userdata);
```

## Function Parameters

|                                                |              |                                                                                   |
| ---------------------------------------------- | ------------ | --------------------------------------------------------------------------------- |
| [SDL_LogOutputFunction](SDL_LogOutputFunction) | **callback** | an [SDL_LogOutputFunction](SDL_LogOutputFunction) to call instead of the default. |
| void *                                         | **userdata** | a pointer that is passed to `callback`.                                           |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetLogOutputFunction](SDL_GetLogOutputFunction)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

