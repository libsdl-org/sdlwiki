###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LogDebug

Log a message with [SDL_LOG_PRIORITY_DEBUG](SDL_LOG_PRIORITY_DEBUG).

## Syntax

```c
void SDL_LogDebug(int category, SDL_PRINTF_FORMAT_STRING const char *fmt, ...) SDL_PRINTF_VARARG_FUNC(2);

```

## Function Parameters

|                  |                                                                       |
| ---------------- | --------------------------------------------------------------------- |
| **category**     | the category of the message                                           |
| **fmt**          | a printf() style message format string                                |
| **...**          | additional parameters matching % tokens in the **fmt** string, if any |

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_Log](SDL_Log)
* [SDL_LogCritical](SDL_LogCritical)
* [SDL_LogError](SDL_LogError)
* [SDL_LogInfo](SDL_LogInfo)
* [SDL_LogMessage](SDL_LogMessage)
* [SDL_LogMessageV](SDL_LogMessageV)
* [SDL_LogVerbose](SDL_LogVerbose)
* [SDL_LogWarn](SDL_LogWarn)

----
[CategoryAPI](CategoryAPI)

