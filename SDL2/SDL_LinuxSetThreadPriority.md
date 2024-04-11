###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LinuxSetThreadPriority

Sets the UNIX nice value for a thread.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_LinuxSetThreadPriority(Sint64 threadID, int priority);

```

## Function Parameters

|                  |                                           |
| ---------------- | ----------------------------------------- |
| **threadID**     | the Unix thread ID to change priority of. |
| **priority**     | The new, Unix-specific, priority value.   |

## Return Value

Returns 0 on success, or -1 on error.

## Remarks

This uses setpriority() if possible, and RealtimeKit if available.

## Version

This function is available since SDL 2.0.9.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

