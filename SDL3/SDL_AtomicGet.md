###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicGet

Get the value of an atomic variable.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
int SDL_AtomicGet(SDL_AtomicInt *a);
```

## Function Parameters

|                                  |       |                                                         |
| -------------------------------- | ----- | ------------------------------------------------------- |
| [SDL_AtomicInt](SDL_AtomicInt) * | **a** | a pointer to an [SDL_AtomicInt](SDL_AtomicInt) variable |

## Return Value

(int) Returns the current value of an atomic variable.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_AtomicSet](SDL_AtomicSet)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

