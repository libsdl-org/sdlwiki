###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_HINT_THREAD_FORCE_REALTIME_TIME_CRITICAL

Specifies whether [SDL_THREAD_PRIORITY_TIME_CRITICAL](SDL_THREAD_PRIORITY_TIME_CRITICAL) should be treated as realtime.

## Header File

Defined in [SDL_hints.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_hints.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
#define SDL_HINT_THREAD_FORCE_REALTIME_TIME_CRITICAL "SDL_THREAD_FORCE_REALTIME_TIME_CRITICAL"
```

## Remarks

On some platforms, like Linux, a realtime priority thread may be subject to
restrictions that require special handling by the application. This hint
exists to let SDL know that the app is prepared to handle said
restrictions.

On Linux, SDL will apply the following configuration to any thread that
becomes realtime: * The SCHED_RESET_ON_FORK bit will be set on the
scheduling policy, * An RLIMIT_RTTIME budget will be configured to the
rtkit specified limit. * Exceeding this limit will result in the kernel
sending SIGKILL to the app, * Refer to the man pages for more information.

This variable can be set to the following values: "0" - default platform
specific behaviour "1" - Force
[SDL_THREAD_PRIORITY_TIME_CRITICAL](SDL_THREAD_PRIORITY_TIME_CRITICAL) to a
realtime scheduling policy

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro)

