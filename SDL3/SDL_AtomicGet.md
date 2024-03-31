###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicGet

Get the value of an atomic variable.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
int SDL_AtomicGet(SDL_AtomicInt *a);

```

## Function Parameters

|           |                                                         |
| --------- | ------------------------------------------------------- |
| **a**     | a pointer to an [SDL_AtomicInt](SDL_AtomicInt) variable |

## Return Value

Returns the current value of an atomic variable.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AtomicSet](SDL_AtomicSet)

----
[CategoryAPI](CategoryAPI), [CategoryAtomic](CategoryAtomic)


