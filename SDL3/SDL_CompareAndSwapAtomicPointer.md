###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CompareAndSwapAtomicPointer

Set a pointer to a new value if it is currently an old value.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
SDL_bool SDL_CompareAndSwapAtomicPointer(void **a, void *oldval, void *newval);
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

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_CompareAndSwapAtomicInt](SDL_CompareAndSwapAtomicInt)
- [SDL_GetAtomicPointer](SDL_GetAtomicPointer)
- [SDL_SetAtomicPointer](SDL_SetAtomicPointer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

