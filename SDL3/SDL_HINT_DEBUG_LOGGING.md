# SDL_HINT_DEBUG_LOGGING

A variable controlling whether SDL logs some debug information.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_DEBUG_LOGGING "SDL_DEBUG_LOGGING"
```

## Remarks

The variable can be set to the following values:

- "0": SDL debug information will not be logged. (default)
- "1": SDL debug information will be logged.

This is generally meant to be used as an environment variable to let
end-users report what subsystems were chosen on their system, perhaps what
sort of hardware they are running on, etc, to aid in debugging. Logged
information is sent through [SDL_Log](SDL_Log)(), which means by default
they appear on stdout on most platforms, or maybe OutputDebugString() on
Windows, and can be funneled by the app with
[SDL_SetLogOutputFunction](SDL_SetLogOutputFunction)(), etc.

The specific output might change between SDL versions; more information
might be deemed useful in the future.

This hint can be set anytime, but the specific logs are generated during
subsystem init.

## Version

This hint is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

