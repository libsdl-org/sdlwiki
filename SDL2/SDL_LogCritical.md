###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LogCritical

Log a message with [SDL_LOG_PRIORITY_CRITICAL](SDL_LOG_PRIORITY_CRITICAL).

## Header File

Defined in [SDL_log.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_log.h)

## Syntax

```c
void SDL_LogCritical(int category, const char *fmt, ...);
```

## Function Parameters

|              |              |                                                                       |
| ------------ | ------------ | --------------------------------------------------------------------- |
| int          | **category** | the category of the message                                           |
| const char * | **fmt**      | a printf() style message format string                                |
| ...          | **...**      | additional parameters matching % tokens in the **fmt** string, if any |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_Log](SDL_Log)
- [SDL_LogDebug](SDL_LogDebug)
- [SDL_LogError](SDL_LogError)
- [SDL_LogInfo](SDL_LogInfo)
- [SDL_LogMessage](SDL_LogMessage)
- [SDL_LogMessageV](SDL_LogMessageV)
- [SDL_LogVerbose](SDL_LogVerbose)
- [SDL_LogWarn](SDL_LogWarn)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

