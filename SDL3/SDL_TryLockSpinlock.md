###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_TryLockSpinlock

Try to lock a spin lock by setting it to a non-zero value.

## Syntax

```c
SDL_bool SDL_TryLockSpinlock(SDL_SpinLock *lock);

```

## Function Parameters

|              |                              |
| ------------ | ---------------------------- |
| **lock**     | a pointer to a lock variable |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the lock succeeded, [SDL_FALSE](SDL_FALSE)
if the lock is already held.

## Remarks

***Please note that spinlocks are dangerous if you don't know what you're
doing. Please be careful using any sort of spinlock!***

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_LockSpinlock](SDL_LockSpinlock)
* [SDL_UnlockSpinlock](SDL_UnlockSpinlock)

----
[CategoryAPI](CategoryAPI)

