# SDL_AtomicIncRef

Increment an atomic variable used as a reference count.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
#define SDL_AtomicIncRef(a)    SDL_AddAtomicInt(a, 1)
```

## Macro Parameters

|       |                                                              |
| ----- | ------------------------------------------------------------ |
| **a** | a pointer to an [SDL_AtomicInt](SDL_AtomicInt) to increment. |

## Return Value

Returns the previous value of the atomic variable.

## Remarks

***Note: If you don't know what this macro is for, you shouldn't use it!***

## Thread Safety

It is safe to call this macro from any thread.

## Version

This macro is available since SDL 3.2.0.

## See Also

- [SDL_AtomicDecRef](SDL_AtomicDecRef)

----
[CategoryAPI](CategoryAPI), [CategoryAPIMacro](CategoryAPIMacro), [CategoryAtomic](CategoryAtomic)

