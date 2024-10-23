###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_CompareAndSwapAtomicPointer

Set a pointer to a new value if it is currently an old value.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
bool SDL_CompareAndSwapAtomicPointer(void **a, void *oldval, void *newval);
```

## Function Parameters

|         |            |                         |
| ------- | ---------- | ----------------------- |
| void ** | **a**      | a pointer to a pointer. |
| void *  | **oldval** | the old pointer value.  |
| void *  | **newval** | the new pointer value.  |

## Return Value

(bool) Returns true if the pointer was set, false otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_CompareAndSwapAtomicInt](SDL_CompareAndSwapAtomicInt)
- [SDL_GetAtomicPointer](SDL_GetAtomicPointer)
- [SDL_SetAtomicPointer](SDL_SetAtomicPointer)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

