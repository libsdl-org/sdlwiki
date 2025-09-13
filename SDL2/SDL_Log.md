# SDL_Log

Log a message with [SDL_LOG_CATEGORY_APPLICATION](SDL_LOG_CATEGORY_APPLICATION) and [SDL_LOG_PRIORITY_INFO](SDL_LOG_PRIORITY_INFO).

## Header File

Defined in [SDL_log.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_log.h)

## Syntax

```c
void SDL_Log(const char *fmt, ...);
```

## Function Parameters

|              |         |                                                                      |
| ------------ | ------- | -------------------------------------------------------------------- |
| const char * | **fmt** | a printf() style message format string.                              |
| ...          | **...** | additional parameters matching % tokens in the `fmt` string, if any. |

## Version

This function is available since SDL 2.0.0.

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

