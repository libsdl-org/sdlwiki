###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SetThreadPriority

Set the priority for the current thread.

## Syntax

```c
int SDL_SetThreadPriority(SDL_ThreadPriority priority);

```

## Function Parameters

|                  |                                                     |
| ---------------- | --------------------------------------------------- |
| **priority**     | the [SDL_ThreadPriority](SDL_ThreadPriority.md) to set |

## Return Value

Returns 0 on success or a negative error code on failure; call
[SDL_GetError](SDL_GetError.md)() for more information.

## Remarks

Note that some platforms will not let you alter the priority (or at least,
promote the thread to a higher priority) at all, and some require you to be
an administrator account. Be prepared for this to fail.

## Version

This function is available since SDL 2.0.0.

----
[CategoryAPI](CategoryAPI.md)
