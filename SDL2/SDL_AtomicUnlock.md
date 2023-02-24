###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AtomicUnlock

Unlock a spin lock by setting it to 0.

## Syntax

```c
void SDL_AtomicUnlock(SDL_SpinLock *lock);

```

## Function Parameters

|              |                              |
| ------------ | ---------------------------- |
| **lock**     | a pointer to a lock variable |

## Remarks

Always returns immediately.

***Please note that spinlocks are dangerous if you don't know what you're
doing. Please be careful using any sort of spinlock!***

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_AtomicLock](SDL_AtomicLock)
* [SDL_AtomicTryLock](SDL_AtomicTryLock)

----
[CategoryAPI](CategoryAPI)

