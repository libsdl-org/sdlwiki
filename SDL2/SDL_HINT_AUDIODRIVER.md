###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_AUDIODRIVER

A variable that decides what audio backend to use.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_AUDIODRIVER "SDL_AUDIODRIVER"
```

## Remarks

By default, SDL will try all available audio backends in a reasonable order
until it finds one that can work, but this hint allows the app or user to
force a specific target, such as "alsa" if, say, you are on PulseAudio but
want to try talking to the lower level instead.

This functionality has existed since SDL 2.0.0 (indeed, before that) but
before 2.0.22 this was an environment variable only. In 2.0.22, it was
upgraded to a full SDL hint, so you can set the environment variable as
usual or programatically set the hint with [SDL_SetHint](SDL_SetHint),
which won't propagate to child processes.

The default value is unset, in which case SDL will try to figure out the
best audio backend on your behalf. This hint needs to be set before
[SDL_Init](SDL_Init)() is called to be useful.

This hint is available since SDL 2.0.22. Before then, you could set the
environment variable to get the same effect.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

