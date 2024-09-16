###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetLogPriorityPrefix

Set the text prepended to log messages of a given priority.

## Header File

Defined in [<SDL3/SDL_log.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_log.h)

## Syntax

```c
SDL_bool SDL_SetLogPriorityPrefix(SDL_LogPriority priority, const char *prefix);
```

## Function Parameters

|                                    |              |                                                                    |
| ---------------------------------- | ------------ | ------------------------------------------------------------------ |
| [SDL_LogPriority](SDL_LogPriority) | **priority** | the [SDL_LogPriority](SDL_LogPriority) to modify.                  |
| const char *                       | **prefix**   | the prefix to use for that log priority, or NULL to use no prefix. |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) on success or
[SDL_FALSE](SDL_FALSE) on failure; call [SDL_GetError](SDL_GetError)() for
more information.

## Remarks

By default [SDL_LOG_PRIORITY_INFO](SDL_LOG_PRIORITY_INFO) and below have no
prefix, and [SDL_LOG_PRIORITY_WARN](SDL_LOG_PRIORITY_WARN) and higher have
a prefix showing their priority, e.g. "WARNING: ".

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetLogPriorities](SDL_SetLogPriorities)
- [SDL_SetLogPriority](SDL_SetLogPriority)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryLog](CategoryLog)

