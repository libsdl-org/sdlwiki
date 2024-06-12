###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetLogPriorities

Set the priority of all log categories.

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
void SDL_SetLogPriorities(SDL_LogPriority priority);
```

## Function Parameters

|                                    |              |                                                  |
| ---------------------------------- | ------------ | ------------------------------------------------ |
| [SDL_LogPriority](SDL_LogPriority) | **priority** | the [SDL_LogPriority](SDL_LogPriority) to assign |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ResetLogPriorities](SDL_ResetLogPriorities)
- [SDL_SetLogPriority](SDL_SetLogPriority)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

