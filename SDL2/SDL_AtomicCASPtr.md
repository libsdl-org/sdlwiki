###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AtomicCASPtr

Set a pointer to a new value if it is currently an old value.

## Header File

Defined in [SDL_atomic.h](https://github.com/libsdl-org/SDL/blob/SDL2/include/SDL_atomic.h)

## Syntax

```c
SDL_bool SDL_AtomicCASPtr(void **a, void *oldval, void *newval);
```

## Function Parameters

|         |            |                         |
| ------- | ---------- | ----------------------- |
| void ** | **a**      | a pointer to a pointer. |
| void *  | **oldval** | the old pointer value.  |
| void *  | **newval** | the new pointer value.  |

## Return Value

([SDL_bool](SDL_bool)) Returns [SDL_TRUE](SDL_TRUE) if the pointer was set,
[SDL_FALSE](SDL_FALSE) otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 2.0.0.

## See Also

- [SDL_AtomicCAS](SDL_AtomicCAS)
- [SDL_AtomicGetPtr](SDL_AtomicGetPtr)
- [SDL_AtomicSetPtr](SDL_AtomicSetPtr)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

