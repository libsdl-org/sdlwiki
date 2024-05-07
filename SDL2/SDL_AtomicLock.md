###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AtomicLock

Lock a spin lock by setting it to a non-zero value.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_atomic.h)

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

This function is available since SDL 2.0.0.

## See Also

- [SDL_AtomicTryLock](SDL_AtomicTryLock)
- [SDL_AtomicUnlock](SDL_AtomicUnlock)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

