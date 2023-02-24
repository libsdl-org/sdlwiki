###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicSet

Set an atomic variable to a value.

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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AtomicGet](SDL_AtomicGet)

----
[CategoryAPI](CategoryAPI), [CategoryAtomic](CategoryAtomic)


