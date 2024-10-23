###### (This is the documentation for SDL3, which is the current stable version. [SDL2](https://wiki.libsdl.org/SDL2/) was the previous version!)
# SDL_memcpy

Copy non-overlapping memory.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void * SDL_memcpy(void *dst, const void *src, size_t len);
```

## Function Parameters

|              |         |                                                                                   |
| ------------ | ------- | --------------------------------------------------------------------------------- |
| void *       | **dst** | The destination memory region. Must not be NULL, and must not overlap with `src`. |
| const void * | **src** | The source memory region. Must not be NULL, and must not overlap with `dst`.      |
| size_t       | **len** | The length in bytes of both `dst` and `src`.                                      |

## Return Value

(void *) Returns `dst`.

## Remarks

The memory regions must not overlap. If they do, use
[SDL_memmove](SDL_memmove)() instead.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.1.3.

## See Also

- [SDL_memmove](SDL_memmove)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

