###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_LinuxSetThreadPriority

Sets the UNIX nice value for a thread.

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

This function is available since SDL 3.0.0.

----
[CategoryAPI](CategoryAPI.md), [CategoryLinux](CategoryLinux.md)
