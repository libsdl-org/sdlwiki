###### (This is the legacy documentation for stable SDL2, the current stable version; [SDL3](https://wiki.libsdl.org/SDL3/) is the current development version.)
# SDL_SIMDRealloc

Reallocate memory obtained from [SDL_SIMDAlloc](SDL_SIMDAlloc.md)

## Syntax

```c
void * SDL_SIMDRealloc(void *mem, const size_t len);

```

## Function Parameters

|             |                                                                                                                                                                                                     |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **mem**     | The pointer obtained from [SDL_SIMDAlloc](SDL_SIMDAlloc.md). This function also accepts NULL, at which point this function is the same as calling [SDL_SIMDAlloc](SDL_SIMDAlloc.md) with a NULL pointer.  |
| **len**     | The length, in bytes, of the block to allocated. The actual allocated block might be larger due to padding, etc. Passing 0 will return a non-NULL pointer, assuming the system isn't out of memory. |

## Return Value

Returns a pointer to the newly-reallocated block, NULL if out of memory.

## Remarks

It is not valid to use this function on a pointer from anything but
[SDL_SIMDAlloc](SDL_SIMDAlloc.md)(). It can't be used on pointers from malloc,
realloc, [SDL_malloc](SDL_malloc.md), memalign, new[], etc.

## Version

This function is available since SDL 2.0.14.

## Related Functions

* [SDL_SIMDGetAlignment](SDL_SIMDGetAlignment.md)
* [SDL_SIMDAlloc](SDL_SIMDAlloc.md)
* [SDL_SIMDFree](SDL_SIMDFree.md)

----
[CategoryAPI](CategoryAPI.md)
