###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetLogPriority

Set the priority of a particular log category.

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
void SDL_SetLogPriority(int category,
                    SDL_LogPriority priority);

```

## Function Parameters

|                  |                                                  |
| ---------------- | ------------------------------------------------ |
| **category**     | the category to assign a priority to             |
| **priority**     | the [SDL_LogPriority](SDL_LogPriority) to assign |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetLogPriority](SDL_GetLogPriority)
- [SDL_ResetLogPriorities](SDL_ResetLogPriorities)
- [SDL_SetLogPriorities](SDL_SetLogPriorities)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

