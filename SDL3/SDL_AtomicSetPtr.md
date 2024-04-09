###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicSetPtr

Set a pointer to a value atomically.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h), but apps should _only_ `#include <SDL3/SDL.h>`!

## Syntax

```c
void* SDL_AtomicSetPtr(void **a, void* v);

```

## Function Parameters

|           |                           |
| --------- | ------------------------- |
| **a**     | a pointer to a pointer    |
| **v**     | the desired pointer value |

## Return Value

Returns the previous value of the pointer.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 3.0.0.

## See Also

* [SDL_AtomicCompareAndSwapPointer](SDL_AtomicCompareAndSwapPointer)
* [SDL_AtomicGetPtr](SDL_AtomicGetPtr)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)


