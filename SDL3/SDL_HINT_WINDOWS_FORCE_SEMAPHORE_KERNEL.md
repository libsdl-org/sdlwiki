###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_WINDOWS_FORCE_SEMAPHORE_KERNEL

A variable controlling whether SDL uses Kernel Semaphores on Windows.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
#define SDL_HINT_WINDOWS_FORCE_SEMAPHORE_KERNEL "SDL_WINDOWS_FORCE_SEMAPHORE_KERNEL"
```

## Remarks

Kernel Semaphores are inter-process and require a context switch on every
interaction. On Windows 8 and newer, the WaitOnAddress API is available.
Using that and atomics to implement semaphores increases performance. SDL
will fall back to Kernel Objects on older OS versions or if forced to by
this hint.

The variable can be set to the following values:

- "0": Use Atomics and WaitOnAddress API when available, otherwise fall
  back to Kernel Objects. (default)
- "1": Force the use of Kernel Objects in all cases.

This hint should be set before SDL is initialized.

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

