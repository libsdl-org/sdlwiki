###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
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

This function is available since SDL 2.0.2.

## Related Functions

* [SDL_AtomicCASPtr](SDL_AtomicCASPtr.md)
* [SDL_AtomicSetPtr](SDL_AtomicSetPtr.md)

----
[CategoryAPI](CategoryAPI.md)
