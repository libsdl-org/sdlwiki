###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetLinuxThreadPriorityAndPolicy

Sets the priority (not nice level) and scheduling policy for a thread.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
bool SDL_SetLinuxThreadPriorityAndPolicy(Sint64 threadID, int sdlPriority, int schedPolicy);
```

## Function Parameters

|                  |                 |                                                                        |
| ---------------- | --------------- | ---------------------------------------------------------------------- |
| [Sint64](Sint64) | **threadID**    | the Unix thread ID to change priority of.                              |
| int              | **sdlPriority** | the new [SDL_ThreadPriority](SDL_ThreadPriority) value.                |
| int              | **schedPolicy** | the new scheduling policy (SCHED_FIFO, SCHED_RR, SCHED_OTHER, etc...). |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This uses setpriority() if possible, and RealtimeKit if available.

## Version

This function is available since SDL 3.1.3.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

