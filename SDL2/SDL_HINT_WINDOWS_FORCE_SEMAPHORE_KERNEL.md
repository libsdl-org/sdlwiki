###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_WINDOWS_FORCE_SEMAPHORE_KERNEL

Force SDL to use Kernel Semaphores on Windows.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

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

This variable can be set to the following values: "0" - Use Atomics and
WaitOnAddress API when available. If not, fall back to Kernel Objects.
(default) "1" - Force the use of Kernel Objects in all cases.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

