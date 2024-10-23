###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_HINT_EVENT_LOGGING

A variable controlling verbosity of the logging of SDL events pushed onto the internal queue.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_EVENT_LOGGING "SDL_EVENT_LOGGING"
```

## Remarks

The variable can be set to the following values, from least to most
verbose:

- "0": Don't log any events. (default)
- "1": Log most events (other than the really spammy ones).
- "2": Include mouse and finger motion events.

This is generally meant to be used to debug SDL itself, but can be useful
for application developers that need better visibility into what is going
on in the event queue. Logged events are sent through [SDL_Log](SDL_Log)(),
which means by default they appear on stdout on most platforms or maybe
OutputDebugString() on Windows, and can be funneled by the app with
[SDL_SetLogOutputFunction](SDL_SetLogOutputFunction)(), etc.

This hint can be set anytime.

## Version

This hint is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

