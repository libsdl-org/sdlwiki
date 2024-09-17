###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_SetAtomicU32

Set an atomic variable to a value.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
Uint32 SDL_SetAtomicU32(SDL_AtomicU32 *a, Uint32 v);
```

## Function Parameters

|                                  |       |                                                                         |
| -------------------------------- | ----- | ----------------------------------------------------------------------- |
| [SDL_AtomicU32](SDL_AtomicU32) * | **a** | a pointer to an [SDL_AtomicU32](SDL_AtomicU32) variable to be modified. |
| Uint32                           | **v** | the desired value.                                                      |

## Return Value

(Uint32) Returns the previous value of the atomic variable.

## Remarks

This function also acts as a full memory barrier.

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAtomicU32](SDL_GetAtomicU32)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

