# SDL_AtomicCAS

Set an atomic variable to a new value if it is currently an old value.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_atomic.h)

## Syntax

```c
SDL_bool SDL_AtomicCAS(SDL_atomic_t *a, int oldval, int newval);
```

## Function Parameters

|                                |            |                                                                       |
| ------------------------------ | ---------- | --------------------------------------------------------------------- |
| [SDL_atomic_t](SDL_atomic_t) * | **a**      | a pointer to an [SDL_atomic_t](SDL_atomic_t) variable to be modified. |
| int                            | **oldval** | the old value.                                                        |
| int                            | **newval** | the new value.                                                        |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the atomic variable
was set, [SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AtomicCASPtr](SDL_AtomicCASPtr)
- [SDL_AtomicGet](SDL_AtomicGet)
- [SDL_AtomicSet](SDL_AtomicSet)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

