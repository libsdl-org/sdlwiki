# SDL_GetAtomicU32

Get the value of an atomic variable.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
Uint32 SDL_GetAtomicU32(SDL_AtomicU32 *a);
```

## Function Parameters

|                                  |       |                                                          |
| -------------------------------- | ----- | -------------------------------------------------------- |
| [SDL_AtomicU32](SDL_AtomicU32) * | **a** | a pointer to an [SDL_AtomicU32](SDL_AtomicU32) variable. |

## Return Value

([Uint32](Uint32)) Returns the current value of an atomic variable.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_SetAtomicU32](SDL_SetAtomicU32)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

