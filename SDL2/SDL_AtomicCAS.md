###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AtomicCAS

Set an atomic variable to a new value if it is currently an old value.

## Syntax

```c
SDL_bool SDL_AtomicCAS(SDL_atomic_t *a, int oldval, int newval);

```

## Function Parameters

|                |                                                                      |
| -------------- | -------------------------------------------------------------------- |
| **a**          | a pointer to an [SDL_atomic_t](SDL_atomic_t.md) variable to be modified |
| **oldval**     | the old value                                                        |
| **newval**     | the new value                                                        |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the atomic variable was set,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_AtomicCASPtr](SDL_AtomicCASPtr.md)
* [SDL_AtomicGet](SDL_AtomicGet.md)
* [SDL_AtomicSet](SDL_AtomicSet.md)

----
[CategoryAPI](CategoryAPI.md)
