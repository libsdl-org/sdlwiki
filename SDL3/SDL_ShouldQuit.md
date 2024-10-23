###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_ShouldQuit

Return whether cleanup should be done.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
bool SDL_ShouldQuit(SDL_InitState *state);
```

## Function Parameters

|                                  |           |                                    |
| -------------------------------- | --------- | ---------------------------------- |
| [SDL_InitState](SDL_InitState) * | **state** | the initialization state to check. |

## Return Value

(bool) Returns true if cleanup needs to be done, false otherwise.

## Remarks

This function checks the passed in state and if cleanup should be done,
sets the status to
[`SDL_INIT_STATUS_UNINITIALIZING`](SDL_INIT_STATUS_UNINITIALIZING) and
returns true.

If this function returns true, the calling code must call
[SDL_SetInitialized](SDL_SetInitialized)() to complete the cleanup.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_SetInitialized](SDL_SetInitialized)
- [SDL_ShouldInit](SDL_ShouldInit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

