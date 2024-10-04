###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_SetInitialized

Finish an initialization state transition.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_SetInitialized(SDL_InitState *state, bool initialized);
```

## Function Parameters

|                                  |                 |                                    |
| -------------------------------- | --------------- | ---------------------------------- |
| [SDL_InitState](SDL_InitState) * | **state**       | the initialization state to check. |
| bool                             | **initialized** | the new initialization state.      |

## Remarks

This function sets the status of the passed in state to
[`SDL_INIT_STATUS_INITIALIZED`](SDL_INIT_STATUS_INITIALIZED) or
[`SDL_INIT_STATUS_UNINITIALIZED`](SDL_INIT_STATUS_UNINITIALIZED) and allows
any threads waiting for the status to proceed.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_ShouldInit](SDL_ShouldInit)
- [SDL_ShouldQuit](SDL_ShouldQuit)


## (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

