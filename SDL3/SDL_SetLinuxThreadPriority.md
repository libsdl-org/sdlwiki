# SDL_SetLinuxThreadPriority

Sets the UNIX nice value for a thread.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
bool SDL_SetLinuxThreadPriority(Sint64 threadID, int priority);
```

## Function Parameters

|                  |              |                                           |
| ---------------- | ------------ | ----------------------------------------- |
| [Sint64](Sint64) | **threadID** | the Unix thread ID to change priority of. |
| int              | **priority** | the new, Unix-specific, priority value.   |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

This uses setpriority() if possible, and RealtimeKit if available.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

