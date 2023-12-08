###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_Log

Log a message with [SDL_LOG_CATEGORY_APPLICATION](SDL_LOG_CATEGORY_APPLICATION.md) and [SDL_LOG_PRIORITY_INFO](SDL_LOG_PRIORITY_INFO.md).

## Syntax

```c
void SDL_Log(SDL_PRINTF_FORMAT_STRING const char *fmt, ...) SDL_PRINTF_VARARG_FUNC(1);

```

## Function Parameters

|             |                                                                     |
| ----------- | ------------------------------------------------------------------- |
| **fmt**     | a printf() style message format string                              |
| **...**     | additional parameters matching % tokens in the `fmt` string, if any |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LogCritical](SDL_LogCritical.md)
* [SDL_LogDebug](SDL_LogDebug.md)
* [SDL_LogError](SDL_LogError.md)
* [SDL_LogInfo](SDL_LogInfo.md)
* [SDL_LogMessage](SDL_LogMessage.md)
* [SDL_LogMessageV](SDL_LogMessageV.md)
* [SDL_LogVerbose](SDL_LogVerbose.md)
* [SDL_LogWarn](SDL_LogWarn.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryLog](CategoryLog.md)
