###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_LinuxSetThreadPriorityAndPolicy

Sets the priority (not nice level) and scheduling policy for a thread.

## Syntax

```c
int SDL_LinuxSetThreadPriorityAndPolicy(Sint64 threadID, int sdlPriority, int schedPolicy);

```

## Function Parameters

|                     |                                                                       |
| ------------------- | --------------------------------------------------------------------- |
| **threadID**        | The Unix thread ID to change priority of.                             |
| **sdlPriority**     | The new [SDL_ThreadPriority](SDL_ThreadPriority.md) value.               |
| **schedPolicy**     | The new scheduling policy (SCHED_FIFO, SCHED_RR, SCHED_OTHER, etc...) |

## Return Value

Returns 0 on success, or -1 on error.

## Remarks

This uses setpriority() if possible, and RealtimeKit if available.

## Version

This function is available since SDL 2.0.18.

----
[CategoryAPI](CategoryAPI.md)
