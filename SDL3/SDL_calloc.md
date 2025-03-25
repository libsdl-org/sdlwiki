# SDL_calloc

Allocate a zero-initialized array.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void * SDL_calloc(size_t nmemb, size_t size);
```

## Function Parameters

|        |           |                                        |
| ------ | --------- | -------------------------------------- |
| size_t | **nmemb** | the number of elements in the array.   |
| size_t | **size**  | the size of each element of the array. |

## Return Value

(void *) Returns a pointer to the allocated array, or NULL if allocation
failed.

## Remarks

The memory returned by this function must be freed with
[SDL_free](SDL_free)().

If either of `nmemb` or `size` is 0, they will both be set to 1.

If the allocation is successful, the returned pointer is guaranteed to be
aligned to either the *fundamental alignment* (`alignof(max_align_t)` in
C11 and later) or `2 * sizeof(void *)`, whichever is smaller.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_free](SDL_free)
- [SDL_malloc](SDL_malloc)
- [SDL_realloc](SDL_realloc)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

