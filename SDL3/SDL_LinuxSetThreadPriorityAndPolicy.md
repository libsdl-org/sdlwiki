###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

This uses setpriority() if possible, and RealtimeKit if available.

## Version

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md), [CategoryLinux](CategoryLinux.md)
