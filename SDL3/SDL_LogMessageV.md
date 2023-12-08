###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LogMessageV

Log a message with the specified category and priority.

## Syntax

```c
void SDL_LogMessageV(int category,
                     SDL_LogPriority priority,
                     SDL_PRINTF_FORMAT_STRING const char *fmt, va_list ap) SDL_PRINTF_VARARG_FUNCV(3);

```

## Function Parameters

|                  |                                        |
| ---------------- | -------------------------------------- |
| **category**     | the category of the message            |
| **priority**     | the priority of the message            |
| **fmt**          | a printf() style message format string |
| **ap**           | a variable argument list               |

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_Log](SDL_Log.md)
* [SDL_LogCritical](SDL_LogCritical.md)
* [SDL_LogDebug](SDL_LogDebug.md)
* [SDL_LogError](SDL_LogError.md)
* [SDL_LogInfo](SDL_LogInfo.md)
* [SDL_LogMessage](SDL_LogMessage.md)
* [SDL_LogVerbose](SDL_LogVerbose.md)
* [SDL_LogWarn](SDL_LogWarn.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryLog](CategoryLog.md)
