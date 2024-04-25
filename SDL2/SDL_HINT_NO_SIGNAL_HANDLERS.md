###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_NO_SIGNAL_HANDLERS

Tell SDL not to catch the SIGINT or SIGTERM signals.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_NO_SIGNAL_HANDLERS   "SDL_NO_SIGNAL_HANDLERS"
```

## Remarks

This hint only applies to Unix-like platforms, and should set before any
calls to [SDL_Init](SDL_Init)()

The variable can be set to the following values:

- "0": SDL will install a SIGINT and SIGTERM handler, and when it catches a
  signal, convert it into an [SDL_QUIT](SDL_QUIT) event.
- "1": SDL will not install a signal handler at all.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryDefine](CategoryDefine), [CategoryHints](CategoryHints)


