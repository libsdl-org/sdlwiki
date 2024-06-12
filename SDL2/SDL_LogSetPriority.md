###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LogSetPriority

Set the priority of a particular log category.

## Header File

Defined in [SDL_log.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_log.h)

## Syntax

```c
void SDL_LogSetPriority(int category,
                    SDL_LogPriority priority);
```

## Function Parameters

|                                    |              |                                                  |
| ---------------------------------- | ------------ | ------------------------------------------------ |
| int                                | **category** | the category to assign a priority to             |
| [SDL_LogPriority](SDL_LogPriority) | **priority** | the [SDL_LogPriority](SDL_LogPriority) to assign |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_LogGetPriority](SDL_LogGetPriority)
- [SDL_LogSetAllPriority](SDL_LogSetAllPriority)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

