###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_THREAD_PRIORITY_POLICY

A string specifying additional information to use with [SDL_SetThreadPriority](SDL_SetThreadPriority).

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h)

## Syntax

```c
#define SDL_HINT_THREAD_PRIORITY_POLICY         "SDL_THREAD_PRIORITY_POLICY"
```

## Remarks

By default [SDL_SetThreadPriority](SDL_SetThreadPriority) will make
appropriate system changes in order to apply a thread priority. For example
on systems using pthreads the scheduler policy is changed automatically to
a policy that works well with a given priority. Code which has specific
requirements can override SDL's default behavior with this hint.

pthread hint values are "current", "other", "fifo" and "rr". Currently no
other platform hint values are defined but may be in the future.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

