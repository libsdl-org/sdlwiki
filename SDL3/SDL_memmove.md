# SDL_memmove

Copy memory ranges that might overlap.

## Header File

Defined in [<SDL3/SDL_stdinc.h>](https://github.com/libsdl-org/SDL/blob/main/include/SDL3/SDL_stdinc.h)

## Syntax

```c
void * SDL_memmove(void *dst, const void *src, size_t len);
```

## Function Parameters

|              |         |                                                  |
| ------------ | ------- | ------------------------------------------------ |
| void *       | **dst** | The destination memory region. Must not be NULL. |
| const void * | **src** | The source memory region. Must not be NULL.      |
| size_t       | **len** | The length in bytes of both `dst` and `src`.     |

## Return Value

(void *) Returns `dst`.

## Remarks

It is okay for the memory regions to overlap. If you are confident that the
regions never overlap, using [SDL_memcpy](SDL_memcpy)() may improve
performance.

## Thread Safety

It is safe to call this function from any thread.

## Version

This function is available since SDL 3.2.0.

## See Also

- [SDL_memcpy](SDL_memcpy)

----
[CategoryAPI](CategoryAPI), [CategoryAPIFunction](CategoryAPIFunction), [CategoryStdinc](CategoryStdinc)

