# SDL_GetAtomicPointer

Get the value of a pointer atomically.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
void * SDL_GetAtomicPointer(void **a);
```

## Function Parameters

|         |       |                         |
| ------- | ----- | ----------------------- |
| void ** | **a** | a pointer to a pointer. |

## Return Value

(void *) Returns the current value of a pointer.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CompareAndSwapAtomicPointer](SDL_CompareAndSwapAtomicPointer)
- [SDL_SetAtomicPointer](SDL_SetAtomicPointer)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

