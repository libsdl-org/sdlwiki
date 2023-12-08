###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_AtomicGetPtr

Get the value of a pointer atomically.

## Syntax

```c
void* SDL_AtomicGetPtr(void **a);

```

## Function Parameters

|           |                        |
| --------- | ---------------------- |
| **a**     | a pointer to a pointer |

## Return Value

Returns the current value of a pointer.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AtomicCASPtr](SDL_AtomicCASPtr.md)
* [SDL_AtomicSetPtr](SDL_AtomicSetPtr.md)

----
[CategoryAPI](CategoryAPI.md), [CategoryAtomic](CategoryAtomic.md)
