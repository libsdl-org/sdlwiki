###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_ShouldInit

Return whether initialization should be done.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
bool SDL_ShouldInit(SDL_InitState *state);
```

## Function Parameters

|                                  |           |                                    |
| -------------------------------- | --------- | ---------------------------------- |
| [SDL_InitState](SDL_InitState) * | **state** | the initialization state to check. |

## Return Value

(bool) Returns true if initialization needs to be done, false otherwise.

## Remarks

This function checks the passed in state and if initialization should be
done, sets the status to
[`SDL_INIT_STATUS_INITIALIZING`](SDL_INIT_STATUS_INITIALIZING) and returns
true. If another thread is already modifying this state, it will wait until
that's done before returning.

If this function returns true, the calling code must call
[SDL_SetInitialized](SDL_SetInitialized)() to complete the initialization.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_SetInitialized](SDL_SetInitialized)
- [SDL_ShouldQuit](SDL_ShouldQuit)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

