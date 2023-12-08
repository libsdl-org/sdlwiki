###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicGet

Get the value of an atomic variable.

## Syntax

```c
int SDL_AtomicGet(SDL_AtomicInt *a);

```

## Function Parameters

|           |                                                         |
| --------- | ------------------------------------------------------- |
| **a**     | a pointer to an [SDL_AtomicInt](SDL_AtomicInt.md) variable |

## Return Value

Returns the current value of an atomic variable.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AtomicSet](SDL_AtomicSet.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAtomic](CategoryAtomic.md)
