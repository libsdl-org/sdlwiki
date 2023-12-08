###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AtomicSetPtr

Set a pointer to a value atomically.

## Syntax

```c
void* SDL_AtomicSetPtr(void **a, void* v);

```

## Function Parameters

|           |                           |
| --------- | ------------------------- |
| **a**     | a pointer to a pointer    |
| **v**     | the desired pointer value |

## Return Value

Returns the previous value of the pointer.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 2.0.2.

## Related Functions

* [SDL_AtomicCASPtr](SDL_AtomicCASPtr.md)
* [SDL_AtomicGetPtr](SDL_AtomicGetPtr.md)

----
[CategoryAPI](CategoryAPI.md)
