###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LogError

Log a message with [SDL_LOG_PRIORITY_ERROR](SDL_LOG_PRIORITY_ERROR.md).

## Syntax

```c
void SDL_LogError(int category, SDL_PRINTF_FORMAT_STRING const char *fmt, ...) SDL_PRINTF_VARARG_FUNC(2);

```

## Function Parameters

|                  |                                                                       |
| ---------------- | --------------------------------------------------------------------- |
| **category**     | the category of the message                                           |
| **fmt**          | a printf() style message format string                                |
| **...**          | additional parameters matching % tokens in the **fmt** string, if any |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_Log](SDL_Log.md)
* [SDL_LogCritical](SDL_LogCritical.md)
* [SDL_LogDebug](SDL_LogDebug.md)
* [SDL_LogInfo](SDL_LogInfo.md)
* [SDL_LogMessage](SDL_LogMessage.md)
* [SDL_LogMessageV](SDL_LogMessageV.md)
* [SDL_LogVerbose](SDL_LogVerbose.md)
* [SDL_LogWarn](SDL_LogWarn.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryLog](CategoryLog.md)
