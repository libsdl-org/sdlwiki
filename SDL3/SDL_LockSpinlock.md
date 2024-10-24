###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_LockSpinlock

Lock a spin lock by setting it to a non-zero value.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
void SDL_LockSpinlock(SDL_SpinLock *lock);
```

## Function Parameters

|                                |          |                               |
| ------------------------------ | -------- | ----------------------------- |
| [SDL_SpinLock](SDL_SpinLock) * | **lock** | a pointer to a lock variable. |

## Remarks

***Please note that spinlocks are dangerous if you don't know what you're
doing. Please be careful using any sort of spinlock!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_TryLockSpinlock](SDL_TryLockSpinlock)
- [SDL_UnlockSpinlock](SDL_UnlockSpinlock)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

