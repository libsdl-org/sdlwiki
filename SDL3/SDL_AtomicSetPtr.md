###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
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

This function is available since SDL 3.0.0.

## Related Functions

* [SDL_AtomicCASPtr](SDL_AtomicCASPtr)
* [SDL_AtomicGetPtr](SDL_AtomicGetPtr)

----
[CategoryAPI](CategoryAPI), [CategoryAtomic](CategoryAtomic)


