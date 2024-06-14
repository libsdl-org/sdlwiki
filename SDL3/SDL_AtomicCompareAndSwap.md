###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicCompareAndSwap

Set an atomic variable to a new value if it is currently an old value.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
SDL_bool SDL_AtomicCompareAndSwap(SDL_AtomicInt *a, int oldval, int newval);
```

## Function Parameters

|                                  |            |                                                                         |
| -------------------------------- | ---------- | ----------------------------------------------------------------------- |
| [SDL_AtomicInt](SDL_AtomicInt) * | **a**      | a pointer to an [SDL_AtomicInt](SDL_AtomicInt) variable to be modified. |
| int                              | **oldval** | the old value.                                                          |
| int                              | **newval** | the new value.                                                          |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the atomic variable
was set, [SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AtomicCompareAndSwapPointer](SDL_AtomicCompareAndSwapPointer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

