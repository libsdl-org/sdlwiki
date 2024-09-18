###### (This is the documentation for SDL3, which is under heavy development and the API is changing! [SDL2](https://wiki.libsdl.org/SDL2/) is the current stable version!)
# SDL_CompareAndSwapAtomicU32

Set an atomic variable to a new value if it is currently an old value.

## Header File

Defined in [<SDL3/SDL_atomic.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_atomic.h)

## Syntax

```c
bool SDL_CompareAndSwapAtomicU32(SDL_AtomicU32 *a, Uint32 oldval, Uint32 newval);
```

## Function Parameters

|                                  |            |                                                                         |
| -------------------------------- | ---------- | ----------------------------------------------------------------------- |
| [SDL_AtomicU32](SDL_AtomicU32) * | **a**      | a pointer to an [SDL_AtomicU32](SDL_AtomicU32) variable to be modified. |
| Uint32                           | **oldval** | the old value.                                                          |
| Uint32                           | **newval** | the new value.                                                          |

## Return Value

(bool) Returns true if the atomic variable was set, false otherwise.

## Remarks

***Note: If you don't know what this function is for, you shouldn't use
it!***

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.0.0.

## See Also

- [SDL_GetAtomicU32](SDL_GetAtomicU32)
- [SDL_SetAtomicU32](SDL_SetAtomicU32)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryAtomic](CategoryAtomic)

