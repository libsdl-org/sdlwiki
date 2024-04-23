###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_HINT_THREAD_PRIORITY_POLICY

A string specifying additional information to use with [SDL_SetThreadPriority](SDL_SetThreadPriority).

## Header File

Defined in [<SDL3/SDL_hints.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_hints.h)

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

On Linux, the kernel may send SIGKILL to realtime tasks which exceed the
distro configured execution budget for rtkit. This budget can be queried
through RLIMIT_RTTIME after calling
[SDL_SetThreadPriority](SDL_SetThreadPriority)().

This hint should be set before calling
[SDL_SetThreadPriority](SDL_SetThreadPriority)()

## Version

This hint is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

