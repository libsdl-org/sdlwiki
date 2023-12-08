###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicLock

Lock a spin lock by setting it to a non-zero value.

## Syntax

```c
void SDL_AtomicLock(SDL_SpinLock *lock);

```

## Function Parameters

|              |                              |
| ------------ | ---------------------------- |
| **lock**     | a pointer to a lock variable |

## Remarks

***Please note that spinlocks are dangerous if you don't know what you're
doing. Please be careful using any sort of spinlock!***

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AtomicTryLock](SDL_AtomicTryLock.md)
* [SDL_AtomicUnlock](SDL_AtomicUnlock.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAtomic](CategoryAtomic.md)
