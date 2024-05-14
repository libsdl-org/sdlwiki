###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_NO_SIGNAL_HANDLERS

Tell SDL not to catch the SIGINT or SIGTERM signals on POSIX platforms.

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_NO_SIGNAL_HANDLERS   "SDL_NO_SIGNAL_HANDLERS"
```

## Remarks

The variable can be set to the following values:

- "0": SDL will install a SIGINT and SIGTERM handler, and when it catches a
  signal, convert it into an [SDL_EVENT_QUIT](SDL_EVENT_QUIT) event.
  (default)
- "1": SDL will not install a signal handler at all.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryHints](CategoryHints)

