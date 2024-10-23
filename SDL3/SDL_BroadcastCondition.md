###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_BroadcastCondition

Restart all threads that are waiting on the condition variable.

## Header File

Defined in [<SDL3/SDL_mutex.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_mutex.h)

## Syntax

```c
void SDL_BroadcastCondition(SDL_Condition *cond);
```

## Function Parameters

|                                  |          |                                   |
| -------------------------------- | -------- | --------------------------------- |
| [SDL_Condition](SDL_Condition) * | **cond** | the condition variable to signal. |

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## Code Examples

```c

// BEWARE: This code example was migrated from the SDL2 Wiki, by only updating the names.

bool condition = false;
SDL_Mutex *lock;
SDL_Condition *cond;
lock = SDL_CreateMutex();
cond = SDL_CreateCondition();

Thread_A:
    SDL_LockMutex(lock);
    while (!condition) {
        SDL_WaitCondition(cond, lock);
    }
    SDL_UnlockMutex(lock);
Thread_B:
    SDL_LockMutex(lock);
    while (!condition) {
        SDL_WaitCondition(cond, lock);
    }
    SDL_UnlockMutex(lock);
Thread_C:
    SDL_LockMutex(lock);
    /* ... */
    condition = true;
    /* ... */
    SDL_BroadcastCondition(cond);
    SDL_UnlockMutex(lock);

SDL_DestroyCondition(cond);
SDL_DestroyMutex(lock);
```

## See Also

- [SDL_SignalCondition](SDL_SignalCondition)
- [SDL_WaitCondition](SDL_WaitCondition)
- [SDL_WaitConditionTimeout](SDL_WaitConditionTimeout)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryMutex](CategoryMutex)

