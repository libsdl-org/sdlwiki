###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LogCritical

Log a message with [SDL_LOG_PRIORITY_CRITICAL](SDL_LOG_PRIORITY_CRITICAL).

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
void SDL_LogCritical(int category, SDL_PRINTF_FORMAT_STRING const char *fmt, ...) SDL_PRINTF_VARARG_FUNC(2);

```

## Function Parameters

|                  |                                                                       |
| ---------------- | --------------------------------------------------------------------- |
| **category**     | the category of the message                                           |
| **fmt**          | a printf() style message format string                                |
| **...**          | additional parameters matching % tokens in the **fmt** string, if any |

## Version

This function is available since SDL 3.0.0.

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


