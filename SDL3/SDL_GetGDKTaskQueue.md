# SDL_GetGDKTaskQueue

Gets a reference to the global async task queue handle for GDK, initializing if needed.

## Header File

Defined in [<SDL3/SDL_system.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_system.h)

## Syntax

```c
bool SDL_GetGDKTaskQueue(XTaskQueueHandle *outTaskQueue);
```

## Function Parameters

|                    |                  |                                                   |
| ------------------ | ---------------- | ------------------------------------------------- |
| XTaskQueueHandle * | **outTaskQueue** | a pointer to be filled in with task queue handle. |

## Return Value

(bool) Returns true on success or false on failure; call
[SDL_GetError](SDL_GetError)() for more information.

## Remarks

Once you are done with the task queue, you should call
XTaskQueueCloseHandle to reduce the reference count to avoid a resource
leak.

## Version

This function is available since SDL 3.2.0.





----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategorySystem](CategorySystem)

