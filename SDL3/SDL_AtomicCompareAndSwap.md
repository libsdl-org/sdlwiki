###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicCompareAndSwap

Set an atomic variable to a new value if it is currently an old value.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
SDL_bool SDL_AtomicCompareAndSwap(SDL_AtomicInt *a, int oldval, int newval);

```

## Function Parameters

|                |                                                                        |
| -------------- | ---------------------------------------------------------------------- |
| **a**          | a pointer to an [SDL_AtomicInt](SDL_AtomicInt) variable to be modified |
| **oldval**     | the old value                                                          |
| **newval**     | the new value                                                          |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the atomic variable was set,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_AtomicCompareAndSwapPointer](SDL_AtomicCompareAndSwapPointer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction)

