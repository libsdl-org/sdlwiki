# SDL_malloc

Allocate uninitialized memory.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void * SDL_malloc(size_t size);
```

## Function Parameters

|        |          |                       |
| ------ | -------- | --------------------- |
| size_t | **size** | the size to allocate. |

## Return Value

(void *) Returns a pointer to the allocated memory, or NULL if allocation
failed.

## Remarks

The allocated memory returned by this function must be freed with
[SDL_free](SDL_free)().

If `size` is 0, it will be set to 1.

If the allocation is successful, the returned pointer is guaranteed to be
aligned to either the *fundamental alignment* (`alignof(max_align_t)` in
C11 and later) or `2 * sizeof(void *)`, whichever is smaller. Use
[SDL_aligned_alloc](SDL_aligned_alloc)() if you need to allocate memory
aligned to an alignment greater than this guarantee.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_free](SDL_free)
- [SDL_calloc](SDL_calloc)
- [SDL_realloc](SDL_realloc)
- [SDL_aligned_alloc](SDL_aligned_alloc)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

