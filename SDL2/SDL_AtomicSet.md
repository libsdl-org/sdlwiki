###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AtomicSet

Set an atomic variable to a value.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_atomic.h)

## Syntax

```c
int SDL_AtomicSet(SDL_atomic_t *a, int v);

```

## Function Parameters

|           |                                                                      |
| --------- | -------------------------------------------------------------------- |
| **a**     | a pointer to an [SDL_atomic_t](SDL_atomic_t) variable to be modified |
| **v**     | the desired value                                                    |

## Return Value

Returns the previous value of the atomic variable.

## Remarks

This function also acts as a full memory barrier.

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 2.0.2.

## See Also

- [SDL_AtomicGet](SDL_AtomicGet)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

