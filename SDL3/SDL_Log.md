###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Log

Log a message with [SDL_LOG_CATEGORY_APPLICATION](SDL_LOG_CATEGORY_APPLICATION) and [SDL_LOG_PRIORITY_INFO](SDL_LOG_PRIORITY_INFO).

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
void SDL_Log(const char *fmt, ...);
```

## Function Parameters

|             |                                                                     |
| ----------- | ------------------------------------------------------------------- |
| **fmt**     | a printf() style message format string                              |
| **...**     | additional parameters matching % tokens in the `fmt` string, if any |

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_LogCritical](SDL_LogCritical)
- [SDL_LogDebug](SDL_LogDebug)
- [SDL_LogError](SDL_LogError)
- [SDL_LogInfo](SDL_LogInfo)
- [SDL_LogMessage](SDL_LogMessage)
- [SDL_LogMessageV](SDL_LogMessageV)
- [SDL_LogVerbose](SDL_LogVerbose)
- [SDL_LogWarn](SDL_LogWarn)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

