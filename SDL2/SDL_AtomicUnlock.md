# SDL_AtomicUnlock

Unlock a spin lock by setting it to 0.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_atomic.h)

## Syntax

```c
void SDL_AtomicUnlock(SDL_SpinLock *lock);
```

## Function Parameters

|                                |          |                               |
| ------------------------------ | -------- | ----------------------------- |
| [SDL_SpinLock](SDL_SpinLock) * | **lock** | a pointer to a lock variable. |

## Remarks

Always returns immediately.

***Please note that spinlocks are dangerous if you don't know what you're
doing. Please be careful using any sort of spinlock!***

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AtomicLock](SDL_AtomicLock)
- [SDL_AtomicTryLock](SDL_AtomicTryLock)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

