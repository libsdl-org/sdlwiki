# SDL_DestroyCond

Destroy a condition variable.

## Header File

Defined in [SDL_mutex.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_mutex.h)

## Syntax

```c
void SDL_DestroyCond(SDL_cond * cond);
```

## Function Parameters

|                        |          |                                    |
| ---------------------- | -------- | ---------------------------------- |
| [SDL_cond](SDL_cond) * | **cond** | the condition variable to destroy. |

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_CondBroadcast](SDL_CondBroadcast)
- [SDL_CondSignal](SDL_CondSignal)
- [SDL_CondWait](SDL_CondWait)
- [SDL_CondWaitTimeout](SDL_CondWaitTimeout)
- [SDL_CreateCond](SDL_CreateCond)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

