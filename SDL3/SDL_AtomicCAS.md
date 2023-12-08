###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicCAS

Set an atomic variable to a new value if it is currently an old value.

## Syntax

```c
SDL_bool SDL_AtomicCAS(SDL_AtomicInt *a, int oldval, int newval);

```

## Function Parameters

|                |                                                                        |
| -------------- | ---------------------------------------------------------------------- |
| **a**          | a pointer to an [SDL_AtomicInt](SDL_AtomicInt.md) variable to be modified |
| **oldval**     | the old value                                                          |
| **newval**     | the new value                                                          |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the atomic variable was set,
[SDL_FALSE](SDL_FALSE.md) otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AtomicCASPtr](SDL_AtomicCASPtr.md)
* [SDL_AtomicGet](SDL_AtomicGet.md)
* [SDL_AtomicSet](SDL_AtomicSet.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAtomic](CategoryAtomic.md)
