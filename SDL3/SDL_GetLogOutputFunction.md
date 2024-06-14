###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_GetLogOutputFunction

Get the current log output function.

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
void SDL_GetLogOutputFunction(SDL_LogOutputFunction *callback, void **userdata);
```

## Function Parameters

|                                                  |              |                                                                                            |
| ------------------------------------------------ | ------------ | ------------------------------------------------------------------------------------------ |
| [SDL_LogOutputFunction](SDL_LogOutputFunction) * | **callback** | an [SDL_LogOutputFunction](SDL_LogOutputFunction) filled in with the current log callback. |
| void **                                          | **userdata** | a pointer filled in with the pointer that is passed to `callback`.                         |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetLogOutputFunction](SDL_SetLogOutputFunction)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

