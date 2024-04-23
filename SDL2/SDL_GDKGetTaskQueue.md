###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_GDKGetTaskQueue

Gets a reference to the global async task queue handle for GDK, initializing if needed.

## Header File

Defined in [SDL_system.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_system.h)

## Syntax

```c
int SDL_GDKGetTaskQueue(XTaskQueueHandle * outTaskQueue);

```

## Function Parameters

|                      |                                                   |
| -------------------- | ------------------------------------------------- |
| **outTaskQueue**     | a pointer to be filled in with task queue handle. |

## Return Value

Returns 0 if success, -1 if any error occurs.

## Remarks

Once you are done with the task queue, you should call
XTaskQueueCloseHandle to reduce the reference count to avoid a resource
leak.

## Version

This function is available since SDL 2.24.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)


