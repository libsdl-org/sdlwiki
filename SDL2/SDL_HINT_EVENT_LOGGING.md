###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_EVENT_LOGGING

A variable controlling verbosity of the logging of SDL events pushed onto the internal queue.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_EVENT_LOGGING   "SDL_EVENT_LOGGING"
```

## Remarks

This variable can be set to the following values, from least to most
verbose:

"0" - Don't log any events (default) "1" - Log most events (other than the
really spammy ones). "2" - Include mouse and finger motion events. "3" -
Include [SDL_SysWMEvent](SDL_SysWMEvent) events.

This is generally meant to be used to debug SDL itself, but can be useful
for application developers that need better visibility into what is going
on in the event queue. Logged events are sent through [SDL_Log](SDL_Log)(),
which means by default they appear on stdout on most platforms or maybe
OutputDebugString() on Windows, and can be funneled by the app with
[SDL_LogSetOutputFunction](SDL_LogSetOutputFunction)(), etc.

This hint can be toggled on and off at runtime, if you only need to log
events for a small subset of program execution.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

