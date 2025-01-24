# SDL_CompareAndSwapAtomicInt

Set an atomic variable to a new value if it is currently an old value.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
bool SDL_CompareAndSwapAtomicInt(SDL_AtomicInt *a, int oldval, int newval);
```

## Function Parameters

|                                  |            |                                                                         |
| -------------------------------- | ---------- | ----------------------------------------------------------------------- |
| [SDL_AtomicInt](SDL_AtomicInt) * | **a**      | a pointer to an [SDL_AtomicInt](SDL_AtomicInt) variable to be modified. |
| int                              | **oldval** | the old value.                                                          |
| int                              | **newval** | the new value.                                                          |

## Return Value

(bool) Returns true if the atomic variable was set, false otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_GetAtomicInt](SDL_GetAtomicInt)
- [SDL_SetAtomicInt](SDL_SetAtomicInt)






----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

