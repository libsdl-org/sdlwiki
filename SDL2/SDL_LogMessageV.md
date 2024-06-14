###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LogMessageV

Log a message with the specified category and priority.

## Header File

Defined in [SDL_log.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_log.h)

## Syntax

```c
void SDL_LogMessageV(int category,
                 SDL_LogPriority priority,
                 const char *fmt, va_list ap);
```

## Function Parameters

|                                    |              |                                         |
| ---------------------------------- | ------------ | --------------------------------------- |
| int                                | **category** | the category of the message.            |
| [SDL_LogPriority](SDL_LogPriority) | **priority** | the priority of the message.            |
| const char *                       | **fmt**      | a printf() style message format string. |
| va_list                            | **ap**       | a variable argument list.               |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_Log](SDL_Log)
- [SDL_LogCritical](SDL_LogCritical)
- [SDL_LogDebug](SDL_LogDebug)
- [SDL_LogError](SDL_LogError)
- [SDL_LogInfo](SDL_LogInfo)
- [SDL_LogMessage](SDL_LogMessage)
- [SDL_LogVerbose](SDL_LogVerbose)
- [SDL_LogWarn](SDL_LogWarn)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

