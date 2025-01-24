# SDL_TryLockSpinlock

Try to lock a spin lock by setting it to a non-zero value.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
bool SDL_TryLockSpinlock(SDL_SpinLock *lock);
```

## Function Parameters

|                                |          |                               |
| ------------------------------ | -------- | ----------------------------- |
| [SDL_SpinLock](SDL_SpinLock) * | **lock** | a pointer to a lock variable. |

## Return Value

(bool) Returns true if the lock succeeded, false if the lock is already
held.

## Remarks

***Please note that spinlocks are dangerous if you don't know what you're
doing. Please be careful using any sort of spinlock!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_LockSpinlock](SDL_LockSpinlock)
- [SDL_UnlockSpinlock](SDL_UnlockSpinlock)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

