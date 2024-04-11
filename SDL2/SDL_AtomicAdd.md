###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AtomicAdd

Add to an atomic variable.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_atomic.h), but apps should _only_ `#include "SDL.h"`!

## Syntax

```c
int SDL_AtomicAdd(SDL_atomic_t *a, int v);

```

## Function Parameters

|           |                                                                      |
| --------- | -------------------------------------------------------------------- |
| **a**     | a pointer to an [SDL_atomic_t](SDL_atomic_t) variable to be modified |
| **v**     | the desired value to add                                             |

## Return Value

Returns the previous value of the atomic variable.

## Remarks

This function also acts as a full memory barrier.

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 2.0.2.

## See Also

* [SDL_AtomicDecRef](SDL_AtomicDecRef)
* [SDL_AtomicIncRef](SDL_AtomicIncRef)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

