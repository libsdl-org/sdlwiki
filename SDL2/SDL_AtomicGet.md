###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AtomicGet

Get the value of an atomic variable.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_atomic.h)

## Syntax

```c
int SDL_AtomicGet(SDL_atomic_t *a);
```

## Function Parameters

|                                |       |                                                        |
| ------------------------------ | ----- | ------------------------------------------------------ |
| [SDL_atomic_t](SDL_atomic_t) * | **a** | a pointer to an [SDL_atomic_t](SDL_atomic_t) variable. |

## Return Value

(int) Returns the current value of an atomic variable.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 2.0.2.

## See Also

- [SDL_AtomicSet](SDL_AtomicSet)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

