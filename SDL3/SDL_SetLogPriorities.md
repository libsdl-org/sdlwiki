# SDL_SetLogPriorities

Set the priority of all log categories.

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
void SDL_SetLogPriorities(SDL_LogPriority priority);
```

## Function Parameters

|                                    |              |                                                   |
| ---------------------------------- | ------------ | ------------------------------------------------- |
| [SDL_LogPriority](SDL_LogPriority) | **priority** | the [SDL_LogPriority](SDL_LogPriority) to assign. |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_ResetLogPriorities](SDL_ResetLogPriorities)
- [SDL_SetLogPriority](SDL_SetLogPriority)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

