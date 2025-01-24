# SDL_SetAtomicPointer

Set a pointer to a value atomically.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
void * SDL_SetAtomicPointer(void **a, void *v);
```

## Function Parameters

|         |       |                            |
| ------- | ----- | -------------------------- |
| void ** | **a** | a pointer to a pointer.    |
| void *  | **v** | the desired pointer value. |

## Return Value

(void *) Returns the previous value of the pointer.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_CompareAndSwapAtomicPointer](SDL_CompareAndSwapAtomicPointer)
- [SDL_GetAtomicPointer](SDL_GetAtomicPointer)


## (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)



----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

