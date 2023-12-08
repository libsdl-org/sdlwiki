###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicTryLock

Try to lock a spin lock by setting it to a non-zero value.

## Syntax

```c
SDL_bool SDL_AtomicTryLock(SDL_SpinLock *lock);

```

## Function Parameters

|              |                              |
| ------------ | ---------------------------- |
| **lock**     | a pointer to a lock variable |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the lock succeeded, [SDL_FALSE](SDL_FALSE.md)
if the lock is already held.

## Remarks

***Please note that spinlocks are dangerous if you don't know what you're
doing. Please be careful using any sort of spinlock!***

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AtomicLock](SDL_AtomicLock.md)
* [SDL_AtomicUnlock](SDL_AtomicUnlock.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAtomic](CategoryAtomic.md)
