###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicCompareAndSwapPointer

Set a pointer to a new value if it is currently an old value.

## Syntax

```c
SDL_bool SDL_AtomicCompareAndSwapPointer(void **a, void *oldval, void *newval);

```

## Function Parameters

|                |                        |
| -------------- | ---------------------- |
| **a**          | a pointer to a pointer |
| **oldval**     | the old pointer value  |
| **newval**     | the new pointer value  |

## Return Value

Returns [SDL_TRUE](SDL_TRUE) if the pointer was set, [SDL_FALSE](SDL_FALSE)
otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AtomicCompareAndSwap](SDL_AtomicCompareAndSwap)
* [SDL_AtomicGetPtr](SDL_AtomicGetPtr)
* [SDL_AtomicSetPtr](SDL_AtomicSetPtr)

----
[CategoryAPI](CategoryAPI)

