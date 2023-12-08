###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_AtomicCASPtr

Set a pointer to a new value if it is currently an old value.

## Syntax

```c
SDL_bool SDL_AtomicCASPtr(void **a, void *oldval, void *newval);

```

## Function Parameters

|                |                        |
| -------------- | ---------------------- |
| **a**          | a pointer to a pointer |
| **oldval**     | the old pointer value  |
| **newval**     | the new pointer value  |

## Return Value

Returns [SDL_TRUE](SDL_TRUE.md) if the pointer was set, [SDL_FALSE](SDL_FALSE.md)
otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Version

This function is available since SDL 2.0.0.

## Related Functions

* [SDL_AtomicCAS](SDL_AtomicCAS.md)
* [SDL_AtomicGetPtr](SDL_AtomicGetPtr.md)
* [SDL_AtomicSetPtr](SDL_AtomicSetPtr.md)

----
[CategoryAPI](CategoryAPI.md)
