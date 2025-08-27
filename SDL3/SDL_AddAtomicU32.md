# SDL_AddAtomicU32

Add to an atomic variable.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
Uint32 SDL_AddAtomicU32(SDL_AtomicU32 *a, int v);
```

## Function Parameters

|                                  |       |                                                                         |
| -------------------------------- | ----- | ----------------------------------------------------------------------- |
| [SDL_AtomicU32](SDL_AtomicU32) * | **a** | a pointer to an [SDL_AtomicU32](SDL_AtomicU32) variable to be modified. |
| int                              | **v** | the desired value to add or subtract.                                   |

## Return Value

([Uint32](Uint32)) Returns the previous value of the atomic variable.

## Remarks

This function also acts as a full memory barrier.

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.4.0.

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

