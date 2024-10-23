###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_aligned_alloc

Allocate memory aligned to a specific alignment.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void * SDL_aligned_alloc(size_t alignment, size_t size);
```

## Function Parameters

|        |               |                              |
| ------ | ------------- | ---------------------------- |
| size_t | **alignment** | the alignment of the memory. |
| size_t | **size**      | the size to allocate.        |

## Return Value

(void *) Returns a pointer to the aligned memory, or NULL if allocation
failed.

## Remarks

The memory returned by this function must be freed with
[SDL_aligned_free](SDL_aligned_free)(), _not_ [SDL_free](SDL_free)().

If `alignment` is less than the size of `void *`, it will be increased to
match that.

The returned memory address will be a multiple of the alignment value, and
the size of the memory allocated will be a multiple of the alignment value.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_aligned_free](SDL_aligned_free)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

